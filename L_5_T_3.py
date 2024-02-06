

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





