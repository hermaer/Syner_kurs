"""
Задание №2
Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. 
Все числа каждого списка находятся на отдельной строке. 
Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

"""

lc1 = input("Введите первый список чисел через пробел: ").split()
lc2 = input("Введите второй список чисел через пробел: ").split()

uc1 = set(lc1)
uc2 = set(lc2)
uc3 = uc1.union(uc2)

print(len(uc3))
