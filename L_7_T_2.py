"""
Задание №2
В первую строчку вводится число N (1 ≤ N ≤ 100 000). 
В следующую строку через пробел вводятся N чисел (1 ≤ Ai ≤ 10e9). 
Вам требуется написать метод, который получает на вход массив и изменяет его таким образом, 
чтобы на первом месте стоял последний элемент, на втором - первый, на третьем - второй и т. д. 
Выведите N чисел - измененный массив.

"""



num = int(input())
my_list = []

while num > 0:
	m = int(input())
	my_list.append(m)
	num -= 1


g = my_list[num-1]
my_list.insert(0, g)
my_list.pop()


print(my_list)
