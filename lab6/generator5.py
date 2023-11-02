def squares(m):
    for i in range(m, 0, -1):
        yield i
    
a = int(input())

b = squares(a)
for n in b:
    print(n, end = ' ')