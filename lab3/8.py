list = input().split() #8
count=1
for i in range(1,len(list)):
    if(list[i] != list[i-1]):
        count=count+1
print(count)

