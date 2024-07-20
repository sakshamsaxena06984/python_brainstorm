import sys
print(sys.version)

print(sys.argv)

"""
os module : interacting with operating system
"""
print("------------ os module -------------")
import os
print(os.getcwd()) # get the current write directory

#print(os.chdir(__path__)) # use to change current directory
# os.mkdir("/Users/sakshamsaxena/PycharmProjects/python_tut/testingos") # use to create the directory
# os.rmdir("/Users/sakshamsaxena/PycharmProjects/python_tut/testingos") # use to delete the directory

# os.remove("__provide the file path __") # use to delete the patn
# os.path.join("__first path for directory location __","__second path for file location __") # use to join the path
# os.path.split("__ path of the directory __") # use to split the path
# print(os.path.exists("/Users/sakshamsaxena/PycharmProjects/python_tut/temp")) # use for checking existing path

"""
subprocess module:
use to interact with operating system and pass the information to the process and then get the return
codes, so it is use to call the function

Math module:
use to perform the mathematics operation
"""

import math
print(math.pi)
print(math.e)
print(math.degrees(0.1))
print(math.acos(0.5))
print(math.asin(0.5))
print(math.atan(45))
print(math.tan(45))
print(math.exp(2))
print(math.log(10,100)) # mean x=10,base 10

"""
Random Module: 
Use to generate the ramdom values
"""
print("------------ random module -------------")
import random
print(random.randrange(0,50))
# for ele in range(1,100):
#     print(f"Random generated value is {random.randrange(0,10)}")
print(random.randrange(0,50,5))
print(random.randint(2,10))

"""
Date Time module:
use for working with date & time
"""
print("------------ datetime module -------------")
import datetime
print(datetime.date.today())
now= datetime.datetime.today()
other= datetime.datetime(1998,10,10,17,59)
print(f"now : {now} and other : {other} and difference is : {now-other}")

"""
JSON module:
JSON stands for JavaScript Object Notation.
It is use for inter communication..
"""
print("------------ json module -------------")
import json
emp_date = """
{
 "people":[
 {
 "name":"Saksham",
 "email":["saks123ham@gmail.com","saxena123saksham@gmail.com"]},
 {
 "name":"ronak",
 "email":["ronak@gmail,com"]
 }
 ]
}
"""
print(emp_date)

emp_date_json=json.loads(emp_date)
print(emp_date_json)
print(emp_date_json['people'])
emp_name=emp_date_json['people']


