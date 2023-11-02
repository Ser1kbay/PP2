a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a==c+2 and b==d+1:
    print("YES")
elif a==c-2 and b==d-1:
    print("YES")
elif a==c+1 and b==d+2:
    print("YES")
elif a==c-1 and b==d-2:
    print("YES")
elif a==c+2 and b==d-1:
    print("YES")
elif a==c-1 and b==d+2:
    print("YES")
elif a==c-2 and b==d+1:
    print("YES")
elif a==c+1 and b==d-2:
    print("YES")
else:
    print("NO")
