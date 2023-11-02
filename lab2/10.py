a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a-c==b-d:
    print("YES")
elif a-c==d-b:
    print("YES")
elif a==c or b==d:
    print("YES")
else:
    print("NO")
