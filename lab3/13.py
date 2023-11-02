list = [int(s) for s in input().split()] #13
counter = 0
for i in range(len(list)):
    for j in range(i + 1, len(list)):
        if list[i] == list[j]:
            counter += 1
print(counter)

