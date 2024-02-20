"""
Урок №16. Классы и объекты
Задание №1

Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
top_up(X) - пополнить на X
count_1000() - выводит сколько целых тысяч осталось в кассе
take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
"""




class Cassa():
	def __init__(self):
		self.bank = 0



	def top_up(self, x):
		self.bank += x


	def count_1000(self):
		ct = self.bank // 1000
		print(f'В банке {ct}т.')


	def take_away(self, X):
		if self.bank < X:
			print("Sorry, you balace very small!")
		else:
			self.bank -= X

b1 = Cassa()

b1.top_up(5600)
print(b1.bank)

b1.count_1000()

b1.take_away(10000)
b1.take_away(150)

print(b1.bank)


