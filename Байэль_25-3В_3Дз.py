

while True:

    user_input = input('\nВведите слово')
    if user_input == 'Выход':
        print('Программа завершена')
        break

    a = len(user_input)
    print('Колличество букв', a)

    c = 'бвгджзйклмнпрстфхцчшщqwrtpsdfghjklzxcvbnm'

    s = 0
    for i in user_input:
        if i in c:
            s += 1
    print('Согласные буквы', s)

    g = 'ioeauiаяуюоеёэиы'

    x = 0
    for i in user_input:
        if i in g:
            x += 1
    print('Гласные буквы', x)

    print(f'Гласные/Согласные:{round(s/len(user_input) * 100,2)}%/{round(x/len(user_input) * 100,2)}%\n')

