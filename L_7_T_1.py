"""
Задание №1
В первой строке вводится число N. 
Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному числу на строке. 
Все числа по модулю не превышают 10e5. 
Переверните массив чисел. Выведите N чисел - перевернутый массив.
"""


a = int(input())
list_n = []

while a > 0:
	a -= 1
	n = int(input())
	list_n.append(n)


list_n.reverse()

print(*list_n)