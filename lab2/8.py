a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a>c+1 or b>d+1:
    print("NO")
elif a<c-1 or b<d-1:
    print("NO")
else:
    print("YES")