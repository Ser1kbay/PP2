def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = input()

first_list = [int(first_list) for first_list in my_list.split()]

new_list = unique_elements(first_list)

print(new_list)
