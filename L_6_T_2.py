
n = int(input('Введите натуральное число: '))
 
count = 0

for i in range(n+1):
	if i > 0 :
		if n % i == 0: 
			count += 1 

print(f"Количество натуральных делителей числа {n}: ", count)	



