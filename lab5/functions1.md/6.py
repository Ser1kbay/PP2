def reverse_sentence(input_string):
    words = input_string.split() 
    reversed_words = ' '.join(reversed(words)) 
    return reversed_words

user_input = input()
reversed_sentence = reverse_sentence(user_input)
print(reversed_sentence)
