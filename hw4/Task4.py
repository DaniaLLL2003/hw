# Задание 5

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_numbers = [num for num in numbers if numbers.count(num) < 2]

print(new_numbers)