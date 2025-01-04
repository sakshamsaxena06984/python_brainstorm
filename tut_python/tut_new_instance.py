
class MyClass:
    def __new__(cls, *args, **kwargs):
        print(f"creating the instance of {cls}")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("Initialization of the class")

if __name__=="__main__":
    obj=MyClass()
