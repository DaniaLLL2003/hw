# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))

def my_func(a, b, c):
    if a > b and a > c:
        if b > c:
            result = print(a + b)
        elif b < c:
            result = print(a + c)
        else:
            result = print('Error')
    elif b > a and b > c:
        if a > c:
            result = print(b + a)
        elif a < c:
            result = print(b + c)
        else:
            result = print('Error')
    elif c > a and c > b:
        if a > b:
            result = print(c + a)
        elif a < b:
            result = print(c + b)
        else:
            result = print('Error')
    else:
        result = print('Error')

my_func(a, b, c)