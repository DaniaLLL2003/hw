# Задание 6a

def z(a, b):
    '''
    a - Число, с которого будет начинаться генератор
    b - Число, с которым закончится генератор
    '''
    while b != a:
        if a > 0:
            if a < b:
                a += 1
                yield print(a)
        elif a < 0:
            if a > b:
                a -= 1
                yield print(a)
        else:
            break

z = z(-1, -5)
next(z)