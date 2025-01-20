"""
Ques 1
30=To
for K in range(0,To)
IF k%4==0:
print (K*4)
Else:
print (K+3)
"""""

#Ans
#to=30
#for k in range(0,to):
 #   if k%4==0:
  #      print(k*4)
   # else:
    #    print(k+3)
    
#ques 2
#find factiorial of nums
"""n=int(input())
factorial=1
if n<0:
    print("negative can not have factorials")
elif n==0:
    print("1")
else:
    for i in range(1,n+1):
        factorial *= i
    print( f"the factorial {n} is {factorial}")"""
    
#ques
"""n=int(input())
for i in range(1,n+1):
    print("*"*i)
"""

#ques 
"""Riya is working on a robotics project where she needs to control the movement of a 
small robot based on sensor inputs. The sensor returns a number representing the 
distance between the robot and an obstacle in front of it. Riya wants to modify the 
robot's movement logic based on whether the distance is an odd number or not. She 
needs a Python program that checks whether the given distance (a number provided 
by the sensor) is odd. If the number is odd, the robot will perform a "right turn"; if 
not, it will continue moving straight."""


#ques
"""n=int(input())
if n%2!=0:
    print("right turn")
else:
    print("keep moving")"""
    
#Q1: Provide a Python Programme that will print the Sin value of the number provided by the user 
#of programme at run time


"""import math 
num=float(input())
print("The sin value of", num, "is", math.sin(num))"""


"""s1="aabbcc"
count=3
while True:
    if s1[0]=='a':
        s1=s1[2:]
    elif s1[-1]=='b':
        s1=s1[:2]
    else:
        count+=1
    break
print(s1)
print(count)"""