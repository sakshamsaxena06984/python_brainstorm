
import collections
import pprint
if __name__=='__main__':
    with open("/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python/demo.txt",'r') as data:
        li=data.read().split(' ')
        print(f"counting of the words in the statement : {len(li)}")
        count_data = collections.Counter(data.read().upper())
        count_value = pprint.pformat(count_data)
    print(count_value)
