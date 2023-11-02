def div(h):
    for i in range(0,h+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
        else:
            continue
    
a = int(input())
b = div(a)
for n in b:
    print(n)