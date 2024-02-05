
a = int(input('Введите пятизначное целое число: '))

a_units = a % 10 
a_tens = (a // 10) % 10
a_hund = (a // 100) % 10
a_thou = (a // 1000) % 10
ten_thou = (a // 10000) % 10

b = a_tens ** a_units
b_hun = b * a_hund
result = b_hun / (ten_thou - a_thou) 

print(result)