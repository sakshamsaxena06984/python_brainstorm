

import queue
if __name__=='__main__':
    q=queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    print(type(q))
    print(q.get())
    print(q.get())
    print(q.empty())
    print(q.qsize())

