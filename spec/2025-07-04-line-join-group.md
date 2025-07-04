# Feature: 使用 LINE 加入團購

## 背景（Business Context）

目前團購流程中，新買家需要註冊帳號才能參與團購，這造成參與門檻過高。希望整合 LINE Login，讓用戶可從 LINE 點擊連結後直接加入團購，提升轉換率。

## 使用者故事（User Story）

作為一位【潛在買家】  
我希望能從 LINE 點選連結快速加入團購  
以便我可以不用註冊帳號即可參與團購

## 驗收條件（Acceptance Criteria）

- [ ] 使用者從 LINE 點連結可打開專屬 join 頁面
- [ ] 若未登入，導引 LINE Login
- [ ] 驗證成功後，將 user_id 寫入 group_participant 表
- [ ] 加入成功後顯示確認頁面

## 輸入資料（Inputs）

```json
{
  "line_token": "string",
  "group_id": "string"
}
```
