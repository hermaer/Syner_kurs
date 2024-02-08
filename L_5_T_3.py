"""

Задание №3
Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма инвестиций - X долларов, 
больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, 
если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

"""

min_invest = int(input("Минимальная сумма инвестиций: "))
maikl_money = int(input("Сумма инвестиций Майкла: "))
ivan_money = int(input("Сумма инвестиций Ивана: "))


if maikl_money >= min_invest and ivan_money >= min_invest:
	print('2')

else:
	if maikl_money >= min_invest:
		print('Mike')
	elif ivan_money >= min_invest:
		print("Ivan")
	elif maikl_money + ivan_money >= min_invest:
		print("1")
	else:
		print("0")







