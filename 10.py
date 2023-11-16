import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case).lower()
    return snake_case
with open('bot.txt', 'r') as file:
    camel_case_string = file.read()

snake_case_string = camel_to_snake(camel_case_string)

print(snake_case_string)
