#regex基礎練習
import re

text = input("輸入字串：")

PatternEmail = r"\b[\w.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+\b"
PatternURL = r"https?://[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+(?:[/?#][^\s]*)?" #(?:...): non-capturing group
PatternIPv4 = (
    r"(?<![\d.])"
    #negative lookbehind:
    #(?<!...): 向前檢查，要求前面內容不符合...
    #[\d.]: 匹配數字或句點
    r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
    r"(?:\.(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}"
    r"(?![\d.])"
    #negative lookahead: 
    #(?!...): 向後檢查，要求後面內容不符合...
)

FindEmail = re.findall(PatternEmail, text)
FindURL = re.findall(PatternURL, text, re.IGNORECASE)
FindIPv4 = re.findall(PatternIPv4, text)
print("Email: {} \nURL: {} \nIPv4: {}".format(FindEmail, FindURL, FindIPv4))