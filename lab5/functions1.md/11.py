def is_palindrome(input_str):
    input_str = input_str.replace(" ", "").lower()
    return input_str == input_str[::-1]

word_or_phrase = input()
if is_palindrome(word_or_phrase):
    print(f"'{word_or_phrase}' is a palindrome.")
else:
    print(f"'{word_or_phrase}' is not a palindrome.")
