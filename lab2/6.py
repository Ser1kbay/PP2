x = int(input())
y = int(input())
z = int(input())
if x==y:
    if x==z:
        print('3')
    else:
        print('2')
elif y==z:
    print('2')
elif x==z:
    print('2')
else:
    print('0')
