#知識卡  #Injection #高二上自主學習

當應用程式未妥善區分使用者輸入與 SQL 指令，將使用者輸入不安全地拼接至 SQL 查詢時，攻擊者可能改變原本 SQL 指令的邏輯，使資料庫執行非預期的操作。

可能造成的影響：

- 未經授權讀取敏感資料。
    
- 修改、刪除或新增資料。
    
- 繞過部分身分驗證機制。
    
- 在特定權限與環境下執行其他資料庫操作。

## 依回傳方式分類

依照攻擊者取得資料的方式，可分為：

- **In-band SQLi（帶內攻擊）**：透過原本的通訊管道取得資料庫回應。
    
    - Error-based：利用錯誤訊息取得資訊。
        
    - UNION-based：將額外查詢結果合併至原本的查詢結果。
    
- **Blind SQLi（盲注攻擊）**：無法直接取得查詢結果，透過應用程式的回應差異間接推測資料。
    
    - Boolean-based：觀察條件不同時的回應差異。
        
    - Time-based：觀察條件不同時的回應時間差異。
    
- **Out-of-band SQLi（帶外攻擊）**：利用原本通訊管道以外的方式傳遞資料，例如 DNS 或 HTTP。

## 依何時執行分類

- **First-order SQLi**：攻擊者輸入惡意內容後，應用程式立即將其不安全地組合進 SQL 查詢，使資料庫執行非預期指令。
	
- **Second-order SQLi**：攻擊者先輸入並儲存惡意內容，之後應用程式在讀取及使用這些資料時，因不安全地組合 SQL 查詢而觸發注入漏洞。

## 防禦方式

- Parameterized Queries（參數化查詢）：將 SQL 指令與使用者輸入分開處理。
    
- Input Validation（輸入驗證）：檢查輸入資料是否符合預期格式。
    
- Least Privilege（最小權限原則）：限制資料庫帳號的操作權限。
    
- Error Handling（錯誤處理）：避免向使用者暴露敏感的資料庫錯誤資訊。
	
- Allow-list validation（白名單輸入驗證）：僅限符合安全格式的資料進入。
	
- ORM / 安全 API：減少手打 SQL 指令。
	
- Stored Procedure（儲存程序）
	
- Web Application Firewall：過濾已知 SQLi 特徵。