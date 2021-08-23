import math as m
from math import pow,sqrt

x = pow(2,3)
print(x)

y = 2**3
print(y)

z = int(input("enter number: "))
a = int(input("enter 2nd number: "))

v = pow(z,a)
print(v)
#we can give expression from user input ...
b = eval(input("enter expression: "))
print(int(b))

def myexp(x):
    result = x**3
    return result
n = int(input("enter number"))
print(myexp(n))
