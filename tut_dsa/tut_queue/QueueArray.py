class Queue:
    def __init__(self):
        self.__arr = []
        self.__count = 0
        self.__front = 0

    def enqueue(self, item):
        self.__arr.append(item)
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            print("queue is empty!")
            return
        data = self.__arr[self.__front]
        self.__count -= 1
        self.__front += 1
        return data

    def top(self):
        if self.__count == 0:
            print("Queue is empty")
            return
        return self.__arr[self.__front]

    def get_size(self):
        return self.__count


if __name__ == '__main__':
    obj = Queue()
    obj.enqueue(3)
    obj.enqueue(2)
    obj.enqueue(1)
    print(f"size of queue : {obj.get_size()}")
    print(f"top element is : {obj.top()}")
    print(f"removed element is : {obj.dequeue()}")
    print(f"size of element is  : {obj.get_size()}")
    print(f"top element is : {obj.top()}")
