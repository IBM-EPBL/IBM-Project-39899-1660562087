
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
n=eval(input("enter no. to find fact:"))
fact=fact(n)
print("fact is",fact)

import math
pi=3.14
r=eval(input("enter the radus:"))
area=(math.pi*r*r)
print("area of circle is",area)
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
if(a>b and a>c):
    print("a is big")
elif(b>c and b>a):
    print("b is big")
else:
    print("c is big")

