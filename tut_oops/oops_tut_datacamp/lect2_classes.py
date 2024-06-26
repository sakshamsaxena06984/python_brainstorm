"""
Adding attributes to a class
After printing ozzy, it is clear that this object is a dog.
But you haven't added any attributes yet. Let's give the Dog class a name and age by rewriting it:
"""


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
You can see that the function now takes two arguments after self: name and age. These then get assigned to self.name and self.age respectively. 
You can now create a new ozzy object with a name and age:
"""

ozzy = Dog("ozzy", 2)

"""
To access an object's attributes in Python, you can use the dot notation. This is done by typing the name of the object, followed by a dot and the attribute's name
"""
print(ozzy)
print(f"access the attributes of class ozzy : name is = {ozzy.name} and age is = {ozzy.age}")
print(ozzy.name + " is " + str(ozzy.age) + " year(s) old.")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def barg(self):
        print("bark bark !")

    def dog_info(self):
        print(f"{self.name} is {self.age} years old")

    def setBuddy(self, buddy):
        self.buddy = buddy
        # buddy.buddy=self


ozzy1 = Dog("ozzy1", 23)
print(ozzy1.name + " " + str(ozzy1.age))
ozzy1.barg()
ozzy1.dog_info()

kupa = Dog("kupa", 4)
kupa.dog_info()
kupa.setBuddy(ozzy1)
kupa.dog_info()
print(f"{kupa.name} buddy is : {kupa.buddy.name} and his age is {kupa.buddy.age}")


