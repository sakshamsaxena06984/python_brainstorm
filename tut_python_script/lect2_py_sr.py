# with open('/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script
# /file_operations/example.txt', 'w') as file:
#     file.write("This is a test.")


# with open('/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script/file_operations/example.txt', 'r') as file:
#     content = file.read()
#     print(content)


# with open("/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script/file_operations/example1.txt",'w') as f:
#     for ele in range(1,100):
#         f.write(f"range processes number us : {ele}")


# with open('/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script/file_operations/example1.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open("/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script/file_operations/example2.txt",'w') as f:
#     for ele in range(1,100):
#         f.write(f"range processes number us : {ele}\n")


# with open('/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python_script/file_operations/example2.txt', 'r') as file:
#     content = file.read()
#     print(content)

import sys
print(sys.argv)

arg1 = sys.argv[1]
arg2 = sys.argv[2]

print(f"first argument is {arg1} and second argument is {arg2}")
