import os
import sys
import re
from github import Github
import openai

# Ensure repository root is on sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

REPO = os.getenv("GITHUB_REPOSITORY")
TOKEN = os.getenv("GITHUB_TOKEN")
API_KEY = os.getenv("INPUT_OPENAI_API_KEY")


def get_pr_number() -> int:
    """Try to get PR number from env or ref."""
    pr_number = os.getenv("PR_NUMBER")
    if pr_number and pr_number.isdigit():
        return int(pr_number)

    ref = os.getenv("GITHUB_REF", "")
    match = re.match(r"refs/pull/(\d+)/", ref)
    if match:
        return int(match.group(1))

    print(f"ERROR: Cannot determine PR number. PR_NUMBER={pr_number}, GITHUB_REF={ref}")
    raise ValueError("Failed to determine PR number.")


def get_pr_diff() -> str:
    """Return aggregated diff text for the pull request."""
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    pr_number = get_pr_number()
    pr = repo.get_pull(pr_number)
    diff_text = ""
    for file in pr.get_files():
        if file.patch:
            diff_text += f"\n--- {file.filename} ---\n{file.patch}\n"
    return diff_text


def run_review(diff: str) -> str:
    """Submit diff to OpenAI and return the review."""
    client = openai.OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "你是一位資安工程師，請審查這段 diff 內容是否有安全性或程式設計問題，並提出具體建議。請以繁體中文回答。",
            },
            {"role": "user", "content": diff[:4000]},
        ],
    )
    return response.choices[0].message.content

def main() -> None:
    print("INFO: CodexReview - fetch_diff")
    diff = get_pr_diff()
    print("INFO: CodexReview - send_to_openai")
    result = run_review(diff)
    print(f"INFO: CodexReview - review_result - {result}")
    try:
        g = Github(TOKEN)
        repo = g.get_repo(REPO)
        pr_number = get_pr_number()
        pr = repo.get_pull(pr_number)
        pr.create_issue_comment(result)
        print("INFO: CodexReview - comment_created")
    except Exception as e:
        print(f"ERROR: CodexReview - comment_failed - {e}")

    critical_issues = ["重大安全問題", "不宜合併", "巨大的安全性風險"]
    if any(issue in result for issue in critical_issues):
        print("ERROR: CodexReview - critical_issue_found")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
