zodiac_day = int(input('Введите день своего рождения:'))
zodiac_month = int(input('Введите месяц своего рождения'))



if (zodiac_day >= 21 and zodiac_day <=31 and zodiac_month == 3) or \
(zodiac_month == 4 and zodiac_day >= 1 and zodiac_day <= 20):
    print('Вы Овен')

elif (zodiac_day >= 21 and zodiac_day <= 31 and zodiac_month == 4) or \
            (zodiac_month == 5 and zodiac_day >= 1 and zodiac_day <= 21):
    print('Вы Телец')

elif (zodiac_day >= 22 and zodiac_day <= 31 and zodiac_month == 5) or \
         (zodiac_month == 6 and zodiac_day >= 1 and zodiac_day <= 21):
    print('Вы Близнецы')

elif (zodiac_day >= 22 and zodiac_day <= 31 and zodiac_month == 6) or \
         (zodiac_month == 7 and zodiac_day >= 1 and zodiac_day <= 22):
    print('Вы Рак')

elif (zodiac_day >= 23 and zodiac_day <= 31 and zodiac_month == 7) or \
         (zodiac_month == 8 and zodiac_day >= 1 and zodiac_day <= 21):
    print('Вы Лев')

elif (zodiac_day >= 22 and zodiac_day <= 31 and zodiac_month == 8) or \
         (zodiac_month == 9 and zodiac_day >= 1 and zodiac_day <= 23):
    print('Вы Дева')

elif (zodiac_day >= 24 and zodiac_day <= 31 and zodiac_month == 9) or \
         (zodiac_month == 10 and zodiac_day >= 1 and zodiac_day <= 23):
    print('Вы Весы')

elif (zodiac_day >= 24 and zodiac_day <= 31 and zodiac_month == 10) or \
         (zodiac_month == 11 and zodiac_day >= 1 and zodiac_day <= 22):
    print('Вы Скорпион')

elif (zodiac_day >= 23 and zodiac_day <= 31 and zodiac_month == 11) or \
         (zodiac_month == 12 and zodiac_day >= 1 and zodiac_day <= 22):
    print('Вы Стрелец')

elif (zodiac_day >= 23 and zodiac_day <= 31 and zodiac_month == 12) or \
         (zodiac_month == 1 and zodiac_day >= 1 and zodiac_day <= 20):
    print('Вы Козерог')

elif (zodiac_day >= 21 and zodiac_day <= 31 and zodiac_month == 1) or \
         (zodiac_month == 2 and zodiac_day >= 1 and zodiac_day <= 19):
    print('Вы Водолей')

elif (zodiac_day >= 20 and zodiac_day <= 31 and zodiac_month == 2) or \
         (zodiac_month == 3 and zodiac_day >= 1 and zodiac_day <= 20):
    print('Вы Рыбы')

else:
    print('Вы ввели не точные данные')