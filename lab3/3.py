list = input().split()  #3
for i in range(1, len(list)):
    if(int(list[i])>int(list[i-1])):
        print(list[i], end=' ')

