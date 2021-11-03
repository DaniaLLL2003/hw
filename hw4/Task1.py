# Задание 1

work_hours = int(input('Выработка в часах: '))
payment_hours = int(input('Ставка в час: '))
prize = int(input('Премия: '))

def earning(a, b, c):
    '''
    a - Выроботка в часах
    b - Ставка в час
    c -  Премия
    '''
    result = (a * b) + c
    return result

print(earning(work_hours, payment_hours, prize))