# Задание 6б

def c(x, y):
    new_list = []
    while len(new_list) != len(x):
        for i in x:
            if x.count(i) < 2:
                new_list.append(i)
                yield print(new_list)
            elif y == len(x):
                break

list = [1, 2, 3, 4, 5,]

c = c(list, 5)
next(c)