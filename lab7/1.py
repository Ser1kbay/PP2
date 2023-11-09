import re
pattern = r'4*'
with open('bot.txt', 'r') as file:
     text = file.read()

a=re.findall(pattern, text)
print(a)