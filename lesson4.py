
# class A(O):...
#
# class B(O):...
# class C(O):...
# class D(O):...
# class E(O):...
# class K1(A, B, C):...
#
# class K2(B, C):...
# class K3(C, D, E):...
# class Z(K1, K2, K3):...


# class O: множественное наследование
#
# class One:
#     def __init__(self, name):
#         self.name = name
#
# class Tho(One):
#     def f(self):
#         print('это функция Tho')
#
#
# class Tho2(One):
#     def tho2(self):
#         print('Эта функция Tho2')
#
# h=Three('Kuba')
#
# h.f()
# print(Three.mro())
#
# class Three(Tho, Tho2): ... наследование
#
# class One:
#     def __init__(self, name):
#         self.name = name
#
# class Tho(One):
#     def f(self):
#         print('это функция Tho')
#
#
# class Tho2(One):
#     def tho2(self):
#         print('Эта функция Tho2')
#
# class Three(Tho, Tho2): ...
#
# h=Three('Kuba')
# h.f()
# print(Three.mro())


 # наследование

class One:
    def __init__(self, name):
        self.name = name

class Tho():
    def __init__(self, age):
        self.age = age
    def f(self):
        print('это функция Tho')


class Tho2(One):
    def tho2(self):
        print('Эта функция Tho2')

class Three(Tho, Tho2):
    # def __init__(self, name, age):
    #     super().__init__(name)
    #     Tho2.__init__(self,name)
    #     Tho2.__init__(self,age)
    def __str__(self):
        return f'{self.name} {self.age}'

c = Three('name')
print(c)