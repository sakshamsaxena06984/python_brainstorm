class MyClass:
    class_variable = 0

    @classmethod
    def incremented_class_variable(cls):
        cls.class_variable += 1
        print(f"updated the value of class_variable : {cls} & value of variable : {cls.class_variable}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_info):
        name, age = person_info.split(",")
        return cls(name, int(age))


if __name__ == "__main__":
    # MyClass.incremented_class_variable()
    # MyClass.incremented_class_variable()

    p = Person.from_string("H,2")
    print(f"info : {p.age} - {p.name}")
