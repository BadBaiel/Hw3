
sum_1r = int(input('укажите сколько градусов в Чуйской области: '))
sum_2r = int(input('укажите сколько градусов в Иссык-Кульской области: '))
sum_3r = int(input('укажите сколько градусов в Таласской области: '))
sum_4r = int(input('укажите сколько градусов в Нарынской области: '))
sum_5r = int(input('укажите сколько градусов в Ошской области: '))
sum_6r = int(input('укажите сколько градусов в Баткенской области: '))
sum_7r = int(input('укажите сколько градусов в Джалал-Абадской области: '))



amount_region = 7

average_degrees = (sum_1r + sum_2r + sum_3r + sum_4r + sum_5r + sum_6r + sum_7r) / amount_region


print('Средний показатель температуры в КР на сегодня', (round(average_degrees, 1)),'°C.')

if (round(average_degrees) >= 20):
        print('Одевайтесь полегче')
elif (round(average_degrees) >= 10 and round(average_degrees) <= 20):
        print('Одевайтесь потеплее на улице прохладно')
else:
        print('Одевайтесь теплее на улице холодно')

