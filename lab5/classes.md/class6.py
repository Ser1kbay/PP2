def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

prime_numbers = set(list(filter(lambda x: is_prime(x), numbers)))


print("Prime numbers in the list:", prime_numbers)
