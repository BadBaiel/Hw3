class Baiel:
    head = 1
    hands = 2
    foots = 2
    def __init__(self, name='Baiel', age=15):
        self.__name = name
        self._age = age
    def __str__(self):
        return f'{self.__name}' \
               f' {self._age}'
    def run(self):
        self._run()
        print(self._age - 1)
        print(self.__name)
    def _run(self):
        print(self.__name, 'run')
a = Baiel()
a.run()
a._run()
print(a._age)
a._age = 11
print(a._age)
#print(a._Baiel__name)

# print(dir(a))
r = 'asdadad'
print(dir(a))
