"""
Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.
"""


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printName(self):
        """

        :return:
        """
        print(f"info about the users :  f{self.firstname} and f{self.lastname}")


'''
child class
'''


class Student(Person):
    pass


p = Person("first", "second")
p.printName()
print(p)

s = Student("first_v1", "second_v1")
s.printName()
print(s)
"""
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
Now we have successfully added the __init__() function, and kept the inheritance of the parent class, 
and we are ready to add functionality in the __init__() function.

Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties 
from its parent:


By using the super() function, you do not have to use the name of the parent element, 
it will automatically inherit the methods and properties from its parent.



"""


class StudentV1(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


s_v1 = StudentV1("sdnk", "smdks")
s_v1.printName()


# via super keyword

class StudentV2(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


s_v2 = StudentV2("student", "V2")
s_v2.printName()


class StudentV3(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year

    def info(self):
        print(f"name of student is {self.firstname} - {self.lastname} and graduated year is : {self.graduationYear}")


s_v3 = StudentV3("smdk", "sdisd", 2023)
s_v3.printName()
s_v3.info()
"""
Python Iterators
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the 
methods __iter__() and __next__().
Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get 
an iterator from.

All these objects have a iter() method which is used to get an iterator:
"""
print("----------  Iterator -------------")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# try:
#     while myit is not None:
#         print(next(myit))
# except NameError:
#     print(f"name of error is {NameError}")


## -> best way of iterating over the iterable object is LOOP

for ele in mytuple:
    print(ele)

"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
The __iter__() method acts similar, you can do operations (initializing etc.), 
but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the next item in the sequence.

"""
print("*********** MyNumbers Class *************")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
