list=input().split() #9
for i in range(0,len(list)):
    if((i+1)%2==0):
        list[i],list[i-1]=list[i-1],list[i]
for i in range(0,len(list)):
    print(list[i],' ')
    
