# merge-sort


# def merging(a1, a2, a):
#     i = 0
#     j = 0
#     k = 0
#     while i < len(a1) and j < len(a2):
#         if a1[i] < a2[j]:
#             a[k] = a1[i]
#             k = k + 1
#             i = i + 1
#         else:
#             a[k] = a2[j]
#             k = k + 1
#             j = j + 1
#     while i < len(a1):
#         a[k] = a1[i]
#         k = k + 1
#         i = i + 1
#     while j < len(a2):
#         a[k] = a2[j]
#         k = k + 1
#         j = j + 1
#
#
# def merge_sort(li):
#
#     if len(li)==1:
#         return
#     mid = len(li) // 2
#     a1 = li[0:mid]
#     a2 = li[mid:]
#     merge_sort(a1)
#     merge_sort(a2)
#     merging(a1, a2, li)
#     print(f"-- {li}")
#
#
# li = [5,4,3,2,1]
# print(f"before performing merge sort : {li}")
# merge_sort(li)
# print(f"after performing merge sort : {li}")


# def fun(a):
#     a=3
#     print(f"inner func: {a}")
# def funli(li):
#     li[0]=1000
# a=1
# fun(a)
#
# li=[2,3,4,5]
# # print(f"after func: {a}")
# print(f"before function call li is {li}")
# funli(li)
# print(f"after function call li is {li}")

print("------------  quick sort ---------------")


def pivot_ele(a, s, e):
    c = s
    pivot = a[s]
    for i in range(s, e + 1):
        if a[i] < pivot:
            c = c + 1
    pivot_index = c + s
    a[s], a[c] = a[c], a[s]
    i = s
    j = e
    while i < c and j > c:
        if a[i] < a[c]:
            i = i + 1
        elif a[j] > a[c]:
            j = j - 1
        else:
            a[i], a[j] = a[j], a[i]
            i = i + 1
            j = j - 1
    # print(f"pivot index is : {pivot_index}")
    return c


def quick_sort(a, s, e):
    if s >= e:
        return
    p_ele = pivot_ele(a, s, e)
    print(f" inner information is : s={s} and e={e} and pi={p_ele}")
    quick_sort(a, s, p_ele - 1)
    quick_sort(a, p_ele + 1, e)


li = [3, 2, 9, 10, 0, 1, 7]
# li=[5,4,3,2,1]
print(f"before quick sort : {li}")
quick_sort(li, 0, len(li) - 1)
print(f"after quick sort : {li}")

print("********************** class and object *************")


class Student:
    pass


s = Student()
s.name = "hello"
s.roll = 6
print(s)
print(type(s))
print(s.__dict__)
print(hasattr(s, "name"))
print(hasattr(s, "name1"))
print(getattr(s, "name1", "not found"))
print(delattr(s, "name"))
print(s.__dict__)

print("------- example of new way ----")


class StudentDetails:
    passingpercentage = 40

    def __init__(self):
        self.name = "rohan"
        self.passingpercentage = 55

    def isPass(self):
        if self.passingpercentage >= StudentDetails.passingpercentage:
            return "pass the exam"
        else:
            return "you have to be check!"

    @staticmethod
    def schoolGreeting():
        print("Welcome to the new school ------------")


ss = StudentDetails()
ss.schoolGreeting()
StudentDetails.schoolGreeting()


class StudentCount:
    total_student = 0

    @classmethod
    def everyCount(cls):
        cls.total_student += 1

    def totalCount(self):
        print(f"total student is : {StudentCount.total_student}")


sc = StudentCount()
sc.totalCount()
sc.everyCount()
sc.totalCount()
sc.everyCount()
sc.totalCount()

print("--------- accesses modifier --------")


class Stu:
    __percentage_req = 40

    def __init__(self, name, age, percent):
        self.__name = name
        self.__age = age
        self.__percentage = percent

    def getDetails(self):
        return f"Student name is {self.__name} and age is {self.__age} and percentage is {self.__percentage}"


s = Stu("hello", 23, 77)
print(s.getDetails())
# print(s.__name) # way of declare private variable
print(s._Stu__percentage_req)
print(s._Stu__name)
print("---------------- inheritance ------------------")


class Vehicle:
    def __init__(self, color, maxSpeed):
        self.color = color
        self.maxSpeed = maxSpeed


class Car(Vehicle):
    def __init__(self, color, maxSpeed, numG):
        super().__init__(color, maxSpeed)
        self.numG = numG

    def printCarDetails(self):
        print(f""" color : {self.color} & maxSpeed is : {self.maxSpeed} and numG is : {self.numG}
                """)


c = Car("red", 333, 5)
c.printCarDetails()

print("------------- another example of inheritance --------------")


class Vehiclev1:
    def __init__(self, color, maxSpeed):
        self.color = color
        self.__maxSpeed = maxSpeed

    def setterMaxSpeed(self, maxSpeed):
        self.__maxSpeed = maxSpeed

    def getterMaxSpeed(self):
        return self.__maxSpeed


class Carv1(Vehiclev1):
    def __init__(self, color, maxSpeed, numG):
        super().__init__(color, maxSpeed)
        self.numG = numG

    def provideDetails(self):
        return f"""
          color is : {self.color} and 
          max_speed is : {self.getterMaxSpeed()} &
          num_gear is : {self.numG}
        """


ss1 = Carv1("pink", 232, 6)
print(ss1.provideDetails())

print("  ----- use of __new__ attribute -----  ")


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, '_initialized'):
            self.value = value
            self._initialized = True


# Testing the Singleton
s1 = Singleton('first')
s2 = Singleton('second')

print(s1.value)  # Output: first
print(s2.value)  # Output: first
print(s1 is s2)  # Output: True
print(Singleton._instance)

print("--------------- use of multi-inheritance -----")


class A:
    def __init__(self, a_name):
        self.a_name = a_name


class B:
    def __init__(self, b_name):
        self.b_name = b_name


class C(A, B):
    def __init__(self, a_name, b_name, c_name):
        A.__init__(self, a_name)
        B.__init__(self, b_name)
        self.c_name = c_name

    def printDetails(self):
        print(f" a name is {self.a_name} & b name is {self.b_name} & c name is {self.c_name}")


c_object = C("A", "B", "C")
print(c_object.printDetails())

print("-----------------  method resolution -------------------")


class Mother:
    def __init__(self):
        print("  ------ mother class call")
        self.name = "Manju"

    def print(self):
        print("Mother name function")


class Father:
    def __init__(self):
        print("  ------ father class call")
        self.name = "Sanju"

    def print(self):
        print("Father name function")


class Child(Mother, Father):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        Father.__init__(self)
        # super().__init__()

    def print(self):
        print(f"name is : {self.name}")


c = Child()
c.print()

print("-----------  operator overload ----------")


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"inner attributes are {self.__x} and {self.__y}"

    def __add__(self, obj_o):
        return Point(self.__x + obj_o.__x, self.__y + obj_o.__y)

    def printDetails(self):
        print(f"informations are : {self.__x} & {self.__y}")


p1 = Point(1, 2)
p2 = Point(11, 22)
p3 = p1 + p2
p1.printDetails()
p3.printDetails()
print(str(p1))

print("-------- abstract class -------")
from abc import ABC


class AutoMobile(ABC):
    def __init__(self):
        print("it is an example of abstract class!")

    @staticmethod
    def start():
        pass

    def second(self):
        print("called via the parent class!")


class Cara(AutoMobile):
    def __init__(self, name):
        self.name = name

    def start(self):
        print("it is an abstract method of parent class!")


obj = Cara("kdjnks")
obj.start()
obj.second()

print("--------------- polymorphism ------------")


def adding(a, b):
    print(f" addition of a and b is {a + b}")


def adding(a, b, c):
    print(f"addition of a and b is {a + b + c}")


adding(1, 2, 3)


class Addi:
    def adding(self, a, b):
        print(f" addition of a and b is {a + b}")

    def adding(self, a, b, c):
        print(f" addition of a and b & c is {a + b + c}")


ob = Addi()
ob.adding(1, 2, 3)


class Animal:
    def sound(self):
        raise NotImplemented("NA")


class Cat(Animal):
    def sound(self):
        return "Meow"


class Dog(Animal):
    def sound(self):
        return "Woof"

animals = [Dog(),Cat()]
for ele in animals:
    print(ele.sound())


