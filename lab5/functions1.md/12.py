def histogram(int_list):
    for num in int_list:
        bar = '*' * num
        print(bar)

values = input()
nums = [int(nums) for nums in values.split()]
histogram(nums)
