import re

def insert_spaces(input_string):
    spaced_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return spaced_string

with open('bot.txt', 'r') as file:
    input_string = file.read()

result = insert_spaces(input_string)

print(result)
