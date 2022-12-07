
left = 1
right = 100
a = 0
numbers = []
while True:
    current = (left + right) // 2
    is_numbers = input('Ваше число:{}?(да- больше- меньше-)'.format(current))
    numbers.append(current)
    a += 1
    if is_numbers.lower() == 'да':
        print('Я угадал!')
        break
    elif is_numbers == 'больше':
        left = current + 1
    elif is_numbers == 'меньше':
        right = current - 1
    else:
        print("Неправильно,введите только эти слова!: 'дa', 'больше' или 'меньше!'")
        with open('results.txt', 'w', encoding='UTF-8') as file:
            file.write(f'Количество попыток-{a}\nСписок попыток-{numbers}\nЗагаданное число-{current}')
