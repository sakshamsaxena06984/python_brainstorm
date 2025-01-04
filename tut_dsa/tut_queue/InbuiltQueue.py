from queue import Queue
"""
for checking top element, we have only get() method, but this method remove the item from the queue
"""
if __name__ == '__main__':
    obj = Queue()
    obj.put(3)
    obj.put(2)
    obj.put(1)
    print(obj.empty())
    print(obj.qsize())
    obj.get()
    print(obj.empty())
    print(obj.qsize())
    print(obj.t)

