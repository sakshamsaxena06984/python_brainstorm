import queue

st=queue.LifoQueue()
st.put(1)
st.put(2)
st.put(3)
print(st.get())
print(st.qsize())
