list = input().split() #7
x=int(input())
c=1
for i in range(0,len(list)):
    if(x<=int(list[i])):
        c=c+1
    else:
        break
print(c)

