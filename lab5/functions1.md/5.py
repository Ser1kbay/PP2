from itertools import permutations

def print_permutations(input_string):
    perm_list = permutations(input_string)
    for perm in perm_list:
        print("".join(perm))
user_input = input("Enter a string: ")
print("Permutations of the string:")
print_permutations(user_input)