import re

def split_at_uppercase(input_string):
    words = re.findall('[A-Z][a-z]*', input_string)
    return ' '.join(words)
with open('bot.txt', 'r') as file:
    input_string = file.read()
result = split_at_uppercase(input_string)

print(result)
