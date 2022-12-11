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
# class SuperHero:
#     people = 'people'
#     def __init__(self,name,nickname,superpower,health_points,catchphrase):
#         self.name=name
#         self.health_points=health_points
#         self.nickname=nickname
#         self.superpower=superpower
#         self.catchphrase=catchphrase
#     def imia(self):
#         print(f'{self.name()}')
#     def nickname(self):
#         print(f'{self.nickname()}')
#     def superpower(self):
#         print(f'{self.superpower()}')
#     def health(self):
#         self.health_points *= 2
#     def catchphrase(self):
#         print(f'{self.catchphrase()}')
#     def __str__(self):
#         return f' name is {self.name}\n' \
#                f' nickname is {self.nickname}\n' \
#                f' superpower is {self.superpower}\n' \
#                f' HP {self.health_points}\n' \
#                f' Catchphrase {self.catchphrase}'
#     def __len__(self):
#         return len(self.catchphrase)
# a = SuperHero('Luffi', 'Mugiwara', 'stretching', 100, 'I Will Be The King Of The Pirates')
# print(a)


# class Robot:
#     brain = True
#
#     def __init__(self, name, model, color, destination):
#         self.name = name
#         self.model = model
#         self.color = color
#         self.destination = destination
#
#     def __str__(self):
#         return f' name is{self.name}\n' \
#                f' color is {self.color}\n' \
#                f' model is {self.model}\n'
#
#     def desti(self):
#         print(self.destination)
#
#
# robot = Robot('Alex', 'A4', 'Blue', 'снимать видео')
# print(robot)
# print(robot.desti())
#
#
# class Robot2(Robot):
#     brain = False
#     def __init__(self, name, model, color, destination, fly):
#         super().__init__(name, model, color, destination)
#         Robot.__init__(self, name, model, color, destination)
#         self.fly = fly
#
#     def desti(self):
#         self.fly = False
#         print(self.fly)
#
#
# robot2 = Robot2(' terminator', 'T228', 'Pink', 'отбирать одежду', True)
# print(robot2.fly)
# robot2.desti()
# print(robot2.fly)
# print(robot2.brain, robot.brain)
#
#
# class Robot3(Robot2):
#     def desti(self):
#         print()
#
# MegaTron=Robot3('TRANsformer', 'Disiptikon', 'Red', 'WARS', False)
# MegaTron.desti()





class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.health_points  = health_points
        self.nickname = nickname
        self.superpower = superpower
        self.catchphrase = catchphrase

    def n(self):
        print(f'Wanted: {self.name}')

    def h(self):
        self.health_points *= 2

    def __str__(self):
        return f'Nickname: {self.nickname}' \
               f'Power: {self.superpower}' \
               f'Health: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero('Monkey D. Luffy', 'Mugiwarra\n', 'Gomu Gomu\n', 70, 'GomuGomuNoPISTOLET')
hero.n()
hero.h()
print(hero)
print(f'Catchphrase: {len(hero.catchphrase)}')

# доч. 1класс
class MagnumHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        aceh = self.health_points ** 2
        self.health_points = aceh

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

ace = MagnumHero('Portgas D. Ace', 'Fire Fist\n', 'Mera Mera\n', 40, 'Dai Enkai Entei')
ace.h()
print(ace)
print(f'Damage: {ace.damage}')
ace.f()
print(f'Fly: {ace.fly}')
ace.phrase()


# доч. 2класс
class DestroyHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def h(self):
        dofih = self.health_points ** 2
        self.health_points = dofih

    def f(self):
        self.fly = True

    def phrase(self):
        print('fly in the True_phrase')

dofi = DestroyHero('Donquixote Doflamingo', 'Heavenly Yaksha\n', 'Ito Ito\n', 60, 'Tori Kago')
dofi.h()
print(dofi)
print(f'Damage: {dofi.damage}')
dofi.f()
print(f'Fly: {dofi.fly}')
dofi.phrase()

# доч. класс от нового класса
class Villain(DestroyHero):
    monster = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)

    def gen_x(self):...

    def crit(self):
        print(f'Crit dm: {self ** 2}')

akainu = Villain('Sakazuki', 'Fleet Admiral\n', 'Magu Magu\n', 90, 'Ryusei Kazan')
print(akainu)
akainu.gen_x()
Villain.crit(ace.damage)

