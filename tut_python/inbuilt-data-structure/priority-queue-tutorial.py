import queue

pq=queue.PriorityQueue()

pq.put(3)
pq.put(2)
pq.put(1)

print(pq.qsize())
print(pq.get())

