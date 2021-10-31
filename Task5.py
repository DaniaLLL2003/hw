# Задание 5

numbers = input('Введите числа через пробел: ').split()
numbers = [int(num) for num in numbers]

def plus(list):
 result = sum(list, 0)
 return result

print(plus(numbers))