class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, item):
        newNode = Node(item)
        newNode.next = self.__head
        self.__head = newNode
        self.__count = self.__count + 1

    def get_size(self):
        return self.__count

    def pop(self):
        if self.get_size() == 0:
            print("Your stack is empty!")
            return
        ele = self.__head.data
        self.__head = self.__head.next
        self.__count = self.__count - 1
        return f"removed item is {ele}"

    def top(self):
        if self.get_size() == 0:
            print("stack is empty")
            return
        return self.__head.data


if __name__ == '__main__':
    obj = Stack()
    obj.push(3)
    obj.push(2)
    obj.push(1)
    print(f"top element of stack is {obj.top()}")
    print(f"size of the link-list-stack is {obj.get_size()}")
    print(obj.pop())
    print(f"size of the link-list-stack is {obj.get_size()}")
    print(f"top element of stack is {obj.top()}")
