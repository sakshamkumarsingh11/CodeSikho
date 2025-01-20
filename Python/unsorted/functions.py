"""
def calculate(a,b):
    sum= a+b
    print(sum)
    return sum
calculate(10,100)"""

#write a fuction to find length
"""Test_Length
def (x):
    l1=len(x)
    print(l1)
    return l1

x=str(input()) 
Test_Length(x)"""

#make a list first
"""list=[input()]
def print_len(list):
    print(len(list))"""


# Fctorial of a number by loop

"""def  fact(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
        print(fact)
       i+=1 
fact(5)"""

#program to find square of any number taken form user

"""def cal_square(n):
    squared= n**2
    print(squared)
    
cal_square(10)    """


#find sum of numbers till n


def sum_num(n):
    if n==0:
        return 0
    else:
        return n+sum_num(n-1)
    
r= sum_num(3)
print(r)