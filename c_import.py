from ctypes import *
so_file = "/home/invlko-014/Desktop/Training_android/my_multiply.so"

my_function = CDLL(so_file)
print(type(my_function))
print("*"*50)
print(my_function.multiply(19,17))