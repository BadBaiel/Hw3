ten = list(range(1, 11))
evens = list(filter(lambda i: i % 2 == 0, ten))
evens1 = list(map(lambda i: i ** 2, evens))
print(ten)
def function(lst=(list(ten))):
    while True:
        index = input("Введите индекс для вывода объекта из списка:")
        if index.lower() == 'exit' or index.lower() == 'Выход':
            break
        try:
                print(lst[int(index)])


        except:
                print('Неверный индекс или данного индекса не существует')
function([1,2,4, True, False, 'sdg', 'try'])





# ten = list(range(1, 11))
# evens = list(filter(lambda i: i % 2 == 0, ten))
# evens1 = list(map(lambda i: i ** 2, evens))
# print(evens1)
#
#
# def function(lst,a=ten):
#     while True:
#         user_input = input('Введите нужный индекс')
#         if user_input == 'exit':
#             print('Программа завершена')
#             break
#         try:
#             print(lst[int(user_input)])
#         except:
#             print('Неверный индекс')




# ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens =[4, 6, 8, 10]
# for i in evens[1:1][1:2][2:3][0:0]:
#     finish = (i**2)
# while True:
#     try:
#         user_input = int(input('Введите индекс'))
#         print(finish)
#     except IndexError:
#      print(f'Неверный индекс. Индекс начинается c 0 до {len[evens]}')
