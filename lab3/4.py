list = input().split()  #4
for i in range(0,len(list)-1):
    if(int(list[i])>0 and int(list[i+1])>0):
        print(list[i],' ',list[i+1])
        return 0
    elif(int(list[i])<0 and int(list[i+1])<0):
        print(list[i],' ',list[i+1])
        return 0


