#7
class1_students = int(input("Введите количество учащихся в первом классе: "))
class2_students = int(input("Введите количество учащихся во втором классе: "))
class3_students = int(input("Введите количество учащихся в третьем классе: "))
total_desks = ((class1_students + 1) // 2 + (class2_students +1) // 2 + (class3_students+1) // 2 )
print( total_desks)