import re

def snake_to_camel(snake_case):
    camel_case = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_case)
    return camel_case

with open('bot.txt', 'r') as file:
    snake_case_string = file.read()
camel_case_string = snake_to_camel(snake_case_string)
print(camel_case_string)
