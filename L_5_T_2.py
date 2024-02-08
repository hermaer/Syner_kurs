"""
Задание №2
Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».
Для решения задачи создайте переменную и в неё положите слово с помощью input()
А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False

т.к. я не знаю как выполнить по другому (используя только тот материал который был предоставлен ранее) делаю как знаю. 

"""


world = input()

count_vowel = 0
count_conso = 0

count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in world:
	if 'a' == i:
		count_vowel += 1
		count_a += 1
	if 'e' == i:
		count_vowel += 1
		count_e += 1
	if 'i' == i:
		count_vowel += 1
		count_i += 1
	if 'o' in i:
		count_vowel += 1
		count_o += 1
	if 'u' in i:
		count_vowel += 1
		count_u += 1

count_conso = len(world) - count_vowel
print("Гласные: ", count_vowel)
print("Согласные: ", count_conso)

print('a' in world, 'Колличество a: ', count_a)
print('e' in world, 'Колличество e: ', count_e)
print('i' in world, 'Колличество i: ', count_i)
print('o' in world, 'Колличество o: ', count_o)
print('u' in world, 'Колличество u: ', count_u)
