import re
with open('row.txt', 'r') as file:
    text = file.read()
tx = re.findall(r"[A-Z][a-z]+", text)
print(tx)