data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
leters = []
number = []
for i in data_tuple:
    if type(i)== str:
        leters.append(i)
    else:
        number.append(i)
number.remove(6.13)
delete = number.pop(0)
leters.append(delete)
number.append(2)
number[1], number[2] = number[2], number[1]
number.sort()
leters.reverse()
leters[1] = leters[1].upper()
leters[-2] = leters[-2].lower()
number[1] = 4
number[2] = 9

print(tuple(leters))
print(tuple(number))
