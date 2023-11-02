list = input().split() #14
for i in range(0, len(list)):
    c=0
    for j in range(0, len(list)):
        if(list[i]==list[j]):
            c=c+1
    if(c==1):
        print(list[i],' ')
        
