list = input().split()  #5
x=0
for i in range(1,len(list)-1):
    if(int(list[i])>int(list[i+1]) and int(list[i])>int(list[i-1])):
        x=x+1
print(x)

