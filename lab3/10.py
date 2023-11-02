list = [int(s) for s in input().split()] #10
imin = 0
imax = 0
for i in range(1, len(list)):
    if list[i] > list[imax]:
        imax = i
    if list[i] < list[imin]:
        imin = i
list[imin], list[imax] = list[imax], list[imin]
print(' '.join([str(i) for i in list]))

