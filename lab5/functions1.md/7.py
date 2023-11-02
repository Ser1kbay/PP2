def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_list = input()
my_list = [int(my_list) for my_list in user_list.split()]
result = has_33(my_list)
print(result)
