def square_generator(N):
    for i in range(1, N+1):
        yield i**2
limit = int(input())
generator = square_generator(limit)
for number in generator:
    print(number)