# Задание 2

numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_numbers = []

def gen(list):
    b = 1
    while b != len(list):
        if list[b] > list[b - 1]:
            new_numbers.append(numbers[b])
            yield print(new_numbers)
        b += 1

a = gen(numbers)
next(a)
next(a)
next(a)
next(a)
next(a)
next(a)