"""
Задание №1
В первую строку вводится число N – количество чисел (1 ≤ N ≤ 100000). 
Во вторую строку вводится через пробел N чисел, каждое не превышает 2*10e9 по модулю. 
Требуется выяснить, сколько среди этих чисел различных. Выведите число, равное количеству различных чисел среди данных.

"""

n = int(input())
numbers = set(map(int, input().split()))

print(len(numbers))