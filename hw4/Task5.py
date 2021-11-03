# Задание 5

from functools import reduce as a

numbers = [num for num in range(100, 1001) if num % 2 == 0]

result = a(lambda x, y: x * y, numbers)

print(result)