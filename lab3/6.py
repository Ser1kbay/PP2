list = input().split() #6
max=-9e10
for i in range(0,len(list)):
    if(int(list[i])>max):
        max=int(list[i])
print(max, end=' ')
for i in range(0,len(list)):
    if(int(list[i])==max):
        print(i)
        break
    
