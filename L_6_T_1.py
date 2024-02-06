

n = int(input("Сколько чисел будет?: "))
count = 0

for i in range(n):
	a = int(input("Число: "))
	if a == 0: 
		count += 1

print(count)



