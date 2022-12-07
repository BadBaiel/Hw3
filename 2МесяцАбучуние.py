# class Human:
#     #атрибуты уравнения класса
#     head=1
#     body=1
#     #фукция : конструктор
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     #метод
#     def run(self):
#         print(f'{self.name} is run')
#
#
# human = Human('Алдияр', 18)
# human.run()
# print()
class SuperHero:
    people = 'people'
    def __init__(self,name,nickname,superpower,health_points,catchphrase):
        self.name=name
        self.health_points=health_points
        self.nickname=nickname
        self.superpower=superpower
        self.catchphrase=catchphrase
    def imia(self):
        print(f'{self.name()}')
    def nickname(self):
        print(f'{self.nickname()}')
    def superpower(self):
        print(f'{self.superpower()}')
    def health(self):
        self.health_points *= 2
    def catchphrase(self):
        print(f'{self.catchphrase()}')
    def __str__(self):
        return f' name is {self.name}\n' \
               f' nickname is {self.nickname}\n' \
               f' superpower is {self.superpower}\n' \
               f' HP {self.health_points}\n' \
               f' Catchphrase {self.catchphrase}'
    def __len__(self):
        return len(self.catchphrase)
a = SuperHero('Luffi', 'Mugiwara', 'stretching', 100, 'I Will Be The King Of The Pirates')
print(a)


