#exercise6.py
#Author:Gudenghao
#17/3/25



def a(n):
    b=1
    for i in range(1,n+1):
         b*=i
    return b
c=int(input("input a number"))
print(a(c))
