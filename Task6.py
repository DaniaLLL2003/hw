# Задание 6

text = input('Введите текст маленькими латинскими буквами ')

def int_func(text):
    latin_text = []
    new_text = text.split()
    for w in new_text:
        w = w.capitalize()
        latin_text.append(w)
    ' '.join(latin_text)
    result = print(latin_text)

    return result

int_func(text)