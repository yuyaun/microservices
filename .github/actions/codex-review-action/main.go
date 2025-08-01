package main

import (
	"context"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/google/go-github/v55/github"
	openai "github.com/sashabaranov/go-openai"
	"golang.org/x/oauth2"
)

func getPRNumber() (int, error) {
	if n := os.Getenv("PR_NUMBER"); n != "" {
		if i, err := strconv.Atoi(n); err == nil {
			return i, nil
		}
	}
	ref := os.Getenv("GITHUB_REF")
	re := regexp.MustCompile(`refs/pull/(\d+)/`)
	if m := re.FindStringSubmatch(ref); len(m) == 2 {
		if i, err := strconv.Atoi(m[1]); err == nil {
			return i, nil
		}
	}
	return 0, fmt.Errorf("cannot determine PR number. PR_NUMBER=%s, GITHUB_REF=%s", os.Getenv("PR_NUMBER"), ref)
}

func parseRepo(repo string) (string, string, error) {
	parts := strings.Split(repo, "/")
	if len(parts) != 2 {
		return "", "", fmt.Errorf("invalid GITHUB_REPOSITORY: %s", repo)
	}
	return parts[0], parts[1], nil
}

func getPRDiff(ctx context.Context, client *github.Client, owner, repo string, prNumber int) (string, error) {
	opt := &github.ListOptions{PerPage: 100}
	diff := ""
	for {
		files, resp, err := client.PullRequests.ListFiles(ctx, owner, repo, prNumber, opt)
		if err != nil {
			return "", err
		}
		for _, f := range files {
			if f.Patch != nil {
				diff += fmt.Sprintf("\n--- %s ---\n%s\n", f.GetFilename(), f.GetPatch())
			}
		}
		if resp.NextPage == 0 {
			break
		}
		opt.Page = resp.NextPage
	}
	return diff, nil
}

func firstN(s string, n int) string {
	if len(s) > n {
		return s[:n]
	}
	return s
}

func runReview(ctx context.Context, diff, apiKey string) (string, error) {
	client := openai.NewClient(apiKey)
	req := openai.ChatCompletionRequest{
		Model: "gpt-4o",
		Messages: []openai.ChatCompletionMessage{
			{
				Role:    openai.ChatMessageRoleSystem,
				Content: "你是一位資安工程師，請審查這段 diff 內容是否有安全性或程式設計問題，並提出具體建議。請以繁體中文回答。",
			},
			{
				Role:    openai.ChatMessageRoleUser,
				Content: firstN(diff, 4000),
			},
		},
	}
	resp, err := client.CreateChatCompletion(ctx, req)
	if err != nil {
		return "", err
	}
	if len(resp.Choices) == 0 {
		return "", fmt.Errorf("no choices returned")
	}
	return resp.Choices[0].Message.Content, nil
}

func main() {
	repoEnv := os.Getenv("GITHUB_REPOSITORY")
	token := os.Getenv("GITHUB_TOKEN")
	apiKey := os.Getenv("INPUT_OPENAI_API_KEY")

	if token == "" {
		fmt.Println("❌ ERROR: GITHUB_TOKEN is not set.")
		os.Exit(1)
	} else {
		fmt.Println("✅ GITHUB_TOKEN received.")
	}

	prNumber, err := getPRNumber()
	if err != nil {
		fmt.Printf("ERROR: %v\n", err)
		os.Exit(1)
	}
	owner, repo, err := parseRepo(repoEnv)
	if err != nil {
		fmt.Printf("ERROR: %v\n", err)
		os.Exit(1)
	}

	ctx := context.Background()
	ts := oauth2.StaticTokenSource(&oauth2.Token{AccessToken: token})
	ghClient := github.NewClient(oauth2.NewClient(ctx, ts))

	fmt.Println("INFO: CodexReview - fetch_diff")
	diff, err := getPRDiff(ctx, ghClient, owner, repo, prNumber)
	if err != nil {
		fmt.Printf("ERROR: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("INFO: CodexReview - send_to_openai")
	result, err := runReview(ctx, diff, apiKey)
	if err != nil {
		fmt.Printf("ERROR: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("INFO: CodexReview - review_result - %s\n", result)

	comment := &github.IssueComment{Body: github.String("🤖 **Codex Review**\n\n" + result)}
	_, _, err = ghClient.Issues.CreateComment(ctx, owner, repo, prNumber, comment)
	if err != nil {
		fmt.Printf("ERROR: failed to create comment: %v\n", err)
		os.Exit(1)
	}

	critical := []string{"重大安全問題", "不宜合併", "巨大的安全性風險"}
	for _, c := range critical {
		if strings.Contains(result, c) {
			fmt.Println("ERROR: CodexReview - critical_issue_found")
			os.Exit(1)
		}
	}
}
