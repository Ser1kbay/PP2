a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a+b)%2==0:
    if (c+d)%2==0:
        print("YES")
    else:
        print("NO")
else:
    if (c+d)%2==0:
        print("NO")
    else:
        print("YES")