
# object oriented programming   ;   basic class and object functionality
# simple class which do nothing


class Simplest:         # class
    pass

simple = Simplest()     # instance of class


# defining class attributes

class Number:
    num = 10            # class attribute

Number.f_num = 13.6     # dynamic addition of attribute

# attributes of class can directly be accessed by class name
print(Number.num)       # 10
print(Number.f_num)     # 13.6

num_obj = Number()      # object/instance of Number
print(num_obj.num)      # 10
print(num_obj.f_num)    # 13.6

num_obj.num = 20        # change the value of num from 10 to 20 but this will not effect the value in class
print(num_obj.num)      # 20
print(Number.num)       # still num == 10


# defining class methods

class Square:
    side = 8

    def area(self):  # self is a reference to an instance
        return self.side ** 2

sq = Square()
print(sq.area())  # 64  ;   object/instance of class


# defining constructor

class Rectangle:
    def __init__(self, sidea, sideb):
        self.sidea = sidea
        self.sideb = sideb

    def area(self):
        return self.sidea * self.sideb


r1 = Rectangle(10, 4)
print(r1.sidea, r1.sideb)   # 10 4
print(r1.area())            # 40
r2 = Rectangle(7, 3)
print(r2.area())            # 21


# inheritance   ;   parent-child relation   ;   IS-A relation

class Human:               # parent class
    def walk(self):
        pass

    def run(self):
        pass

    def sleep(self):
        pass


class Boy(Human):           # child class   ;   Boy IS-A Human
    pass


# composition   ;   HAS-A relation

class Engine:
    def start(self):
        pass


class Car:
    engine_class = Engine

    def __init__(self):
        self.engine = self.engine_class         # Car HAS-A Engine


# method overriding

class Parent:           # parent class
        def do_work(self):
            print('Parent work')


class Child(Parent):    # child class
        def do_work(self):
            print('Child work')

c = Child()             # instance of child
c.do_work()            # child calls overridden method


# method and attribute hiding   ;   we can hide them using dunder (__) before their name

class Boss:
    __account_num = 12345

    def do_work(self):
        print('i m accessible from outside of class.')

    def __do_not_work(self):
        print('i m not accessible from outside of class')

b = Boss()
# print(b.__account)   raise exception ; AttributeError: 'Boss' object has no attribute '__account'
b.do_work()            # i m accessible.
# b.__do_not_work()    AttributeError: 'Boss' object has no attribute '__do_not_work'


# python supports multiple inheritance by mean of MRO (method resolution object)

class A:
    def do(self):
        print('In A')


class B:
    def do(self):
        print('In B')


class C(A):                 # C inherits A
    def do(self):           # C do override A do
        print('In C')


class D(B, C):              # D inherits B and C
    pass


# now lets see if we call do what will print

d = D()
d.do()                      # In B  ;   which means a/c mro left most has higher precedence
print(d.__class__.mro())    # class D first goes to class class B than C than C to A
