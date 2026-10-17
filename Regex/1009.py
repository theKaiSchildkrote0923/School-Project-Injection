import re #re: regex函式庫

text = "Contact us at support@example.com or admin@domain.org. james.ku@jameskool.com james.ku@bb.cc Jake-kk@gmail.com"
pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,63}" #regex判斷
email = re.findall(pattern, text) #找尋text中所有符合的部分
print(email)
email = re.search(pattern, text) #找尋text中第一個符合的部分
if email:
    print("找到的第一筆：", email.group())
email = re.sub(pattern, "email", text) #將符合的部分以email替代
print(email)