#知識卡 #高二上自主學習 

CSRF （Cross- Site Request Forgery）是一種 Web Security 漏洞，攻擊者利用使用者已登入網站的身分，誘使其瀏覽器向該網站發送非預期的請求。**不是 Injection** （[[Injection MOC]]）。

當瀏覽器自動附帶有效的登入 Cookie，而伺服器又未妥善驗證請求是否由使用者主動發起時，便可能執行未經授權的操作。

可能造成的影響：

- 修改帳戶設定。
    
- 發送訊息或執行其他帳戶操作。
    
- 在特定條件下進行非預期交易。

## 防禦方式

- **CSRF Token**：要求重要請求附帶伺服器提供的有效驗證 Token。
    
- **SameSite Cookie**：限制跨網站請求是否附帶登入 Cookie。
    
- **Origin / Referer Validation**：檢查請求來源是否符合預期。
    
- **Re-authentication**：重要操作前要求重新驗證使用者身分。
    
- **Safe HTTP Methods**：GET 等安全方法不應執行資料修改等狀態變更操作。