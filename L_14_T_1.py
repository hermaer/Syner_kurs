"""
Урок №14. Рекурсия
Задание №1
Есть последовательность
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
Напишите рекурсивную функцию, которая выведет все элементы от первого до последнего 
и в конце отобразит сообщение Конец списка, если выводить больше нечего. Циклы использовать запрещено
"""

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def req(n=0):
	if n == len(my_list):
		return print("Конец списка")
	print(my_list[n])
	req(n+1)

req()

