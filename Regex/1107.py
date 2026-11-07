import re

# re.ASCII shorthand: re.A
text = "Käfig"
pattern = r"\w"
print(re.findall(pattern, text)) # ['K', 'ä', 'f', 'i', 'g']
print(re.findall(pattern, text, re.ASCII)) # ['K', 'f', 'i', 'g']

# re.UNICODE shorthand: re.U
text = "Käfig"
pattern = r"\w"
print(re.findall(pattern, text, re.UNICODE)) # ['K', 'ä', 'f', 'i', 'g']
print(re.findall(pattern, text)) # ['K', 'ä', f', 'i', 'g']

# re.DEBUG
text = "Hello World!"
pattern = r"He.*o"
print(re.findall(pattern, text, re.DEBUG)) # 顯示 python 如何解析 regex

# re.DOTALL shorthand: re.S
text = """Hello,
my
name
is
Kai."""
pattern = r"my.name"
print(re.findall(pattern, text, re.DOTALL))
# ['my\nname'] '.'配對任意字符（包含換行）
print(re.findall(pattern, text)) # []

# re.IGNORECASE shorthand: re.I
text = "Hello World!"
print(re.findall(r"Hello", text, re.IGNORECASE)) # ['Hello']
print(re.findall(r"hello", text, re.IGNORECASE)) # ['Hello']

# re.MULTILINE shorthand: re.M
text = """Hello
Hello
Hello"""
pattern = r"^Hello"
print(re.findall(pattern, text, re.MULTILINE)) # ['Hello', 'Hello', 'Hello]
print(re.findall(pattern, text)) # ['Hello']

# re.VERBOSE shorthand: re.X
text = "Hello Helloween HeyHello"
pattern = """
[A-Za-z]* # 任意字母開頭
Hello+ # 中間包含 Hello
[a-z]* # 後面跟著任意小寫字母
"""
print(re.findall(pattern, text, re.VERBOSE)) # ['Hello', 'Helloween', 'HeyHello']
print(re.findall(pattern, text)) # []