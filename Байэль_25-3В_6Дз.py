"""1.Написать функцию, которая возвращает первое слово из полученного предложения."""

def words(meaning):
    if type(meaning) == str:
        meaning = meaning.split()
        print(meaning[0])
    else:
        return False
words('Bonjour etranger!')


"""2.Написать функцию, которая принимает неограниченное количество чисел и возвращает их среднее арифметическое."""



def number_plus(a, *args, b=0):
    print(f'a: {a}, b: {b}, args: {args}')
    return sum(args) / a
print(round(number_plus(2, 4, 6, 8, 56),0))

"""3.Написать функцию, проверяющую надежность пароля."""

def password(complexity=input('Введите пароль: ')):
    if len(complexity) >= 6 and not complexity.isdigit() and not complexity.isalpha():
        return True
    else:
        return False
password()









