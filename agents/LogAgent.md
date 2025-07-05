# Agent: LogAgent

## Purpose

`LogAgent` 定義本地 log 撰寫的標準，提供一套統一的 logging 函式呼叫方式。其他 Agent 必須依照本規範記錄執行過程中的重要事件，幫助後續除錯、追蹤與任務回放。

---

## Logging Guidelines

- 使用 `log_event(agent: str, event: str, data: dict, level: str = "INFO")`。
- 必須記錄：
    - 任務開始 / 結束
    - API 呼叫
    - 外部資源存取
    - 錯誤情況
    - HTTP 請求接收與發送
    - Kafka 訊息接收與發送
- 請使用 `JSON` 格式記錄內容，必要欄位為：
    - `ts`: timestamp
    - `agent`: 呼叫的 agent 名稱
    - `event`: 動作名稱
    - `level`: "DEBUG" | "INFO" | "WARN" | "ERROR"
    - `data`: 任意 dict，包含 context、payload、trace_id 等資訊。
- 不可記錄：密碼、token、機敏資訊。
- 預設 log 輸出為 terminal 和本地 `agent_log.jsonl` 檔案。

---
