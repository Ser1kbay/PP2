def squares(h,m):
    for i in range(h,m+1):
        yield i**2
    
a = int(input())
c = int(input())
b = squares(a,c)
for n in b:
    print(n,end=' ')