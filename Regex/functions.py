import re #re: regex函式庫

text = "Contact us at support@example.com or admin@domain.org. james.ku@jameskool.com james.ku@bb.cc Jake-kk@gmail.com"
pattern = r"[\w.-]+@[\w.-]+\.[a-zA-Z]{2,63}"

# re.findall()
email = re.findall(pattern, text) # 找尋 text 中所有符合的部分，找不到則回傳空 list
print(email)

# re.search()
email = re.search(pattern, text) # 回傳 Match Object，若不只一個部份符合，將回傳第一個，找不到則回傳 None
if email:
    print("找到的第一筆：", email.group())

# Match Object: 包含搜索內容與結果，找不到則回傳 None
# .span(): 輸出目標的位置，(開頭, 結尾)
# .string: 輸出 text 的內容
# .group(): 輸出找到的結果

# re.sub()
email = re.sub(pattern, "email", text) # 將符合的部分以 "email" 替代
print(email)
email = re.sub(pattern, "email", text, 2) # count: 取代幾個
print(email)

# re.split()
email = re.split(r"\s", text) # 以空格作為分裂點，將前後分開
print(email)
email = re.split(r"\s", text, 5) # maxsplit: 拆分的上限
print(email)