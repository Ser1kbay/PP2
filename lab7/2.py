import re
with open('row.txt', 'r') as file:
    text = file.read()
tx = re.findall(r"ab{2,3}", text)
print(tx)

