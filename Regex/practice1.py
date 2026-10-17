import re

text = input("輸入字串：")

PatternEmail = r"\b[\w.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+\b"
PatternURL = r"https?://[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:[/?#][^\s]*)?" #(?:...)
PatternIPv4 = (
    r"(?<![\d.])" #前面不能緊接著數字或句點
    r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    r"(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}"
    r"(?![\d.])" #後面不能緊接著數字或句點
)

FindEmail = re.findall(PatternEmail, text)
FindURL = re.findall(PatternURL, text, re.IGNORECASE)
FindIPv4 = re.findall(PatternIPv4, text)
print("Email: {} \nURL: {} \nIPv4: {}".format(FindEmail, FindURL, FindIPv4))