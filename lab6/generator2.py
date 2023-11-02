def evennum(h):
    for i in range(0,h+1):
        if i % 2 == 0:
            yield i
        else:
            continue
    
a = int(input())
b = evennum(a)
for n in b:
    print(n)