# AGENTS.md

本專案使用多個 Agent 概念模組，協助進行自動化開發、重構與文件生成。

## 🧠 Agents 一覽

| Agent 名稱          | 功能描述                           | 檔案位置                     |
| ------------------- | ---------------------------------- | ---------------------------- |
| KafkaBot            | 設定與使用 Kafka topic 與 consumer | `agents/KafkaBot.md`         |
| ApiBot              | 建立 REST API 並維持一致命名與結構 | `agents/ApiBot.md`           |
| DocsBot             | 撰寫 README、docstring、文件產生器 | `agents/DocsBot.md`          |
| RefactorBot         | 重構舊有程式碼、改善可讀性與品質   | `agents/RefactorBot.md`      |
| TestGenie           | 自動產生 pytest 測試               | `agents/TestGenie.md`        |
| BugHunter           | 偵錯與分析程式錯誤                 | `agents/BugHunter.md`        |
| RequirementAgent.md | 需求分析與功能規劃                 | `agents/RequirementAgent.md` |

## 💡 說明

- 每個 agent 都為 AI 專屬的角色設定檔
- 可搭配 LLM IDE（如 Continue）、ChatGPT 插件、LangChain Agent 使用
- 可轉換為 `.json` 形式供自動化工具使用
