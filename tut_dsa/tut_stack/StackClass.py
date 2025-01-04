class Stack:
    def __init__(self):
        self.__data = []

    def push(self, ele):
        self.__data.append(ele)

    def get_size(self):
        return len(self.__data)

    def pop(self):
        if self.get_size() == 0:
            print("Stack is empty")
            return
        self.__data.pop()

    def printing(self):
        print("all elements of stack!")
        for ele in self.__data:
            print(ele)


if __name__=='__main__':
    obj=Stack()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    obj.printing()
    print(f"size of stack is {obj.get_size()}")
    obj.pop()
    obj.printing()
