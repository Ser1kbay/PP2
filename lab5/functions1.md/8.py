def spy_game(nums):
    zero_count = 0
    for num in nums:
        if num == 0 and zero_count < 2:
            zero_count += 1
        elif num == 7 and zero_count == 2:
            return True
    return False

user_input = input()
user_list = [int(num) for num in user_input.split()]

result = spy_game(user_list)
print(result)

