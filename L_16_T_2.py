"""
Задание №2

Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек,
на которое она перемещается за ход 
у этого класс есть методы:
go_up() - увеличивает y на s
go_down() - уменьшает y на s
go_left() - уменьшает x на s
go_right() - увеличивает y на s
evolve() - увеличивает s на 1
degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться
до x2 y2 от текущей позиции

"""

class turtle():
	def __init__(self):
		self.x = 0 
		self.y = 0
		self.s = 1

	def go_up(self):
		self.y += self.s

	def go_down(self):
		self.y -= self.s

	def go_left(self):
		self.x -= self.s 

	def go_right(self):
		self.x += self.s

	def degrade(self):
		if self.s <= 0:
			print("Sorry, you speed low")
		else:
			self.s -= 1

	def evolve(self):
		self.s += 1

	def count_moves(x2, y2):
		r_x = x2 - self.x
		r_y = y2 - self.y
		count = 0
		if r_x < 0:
			r_x *= -1
		if r_y < 0:
			r_y *= -1

		moves_x = r_x // self.s + (1 if r_x % self.s != 0 else 0)
		moves_y = r_y // self.s + (1 if r_y % self.s != 0 else 0)

		return moves_x + moves_y
















