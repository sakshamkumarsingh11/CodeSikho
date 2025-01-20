"""Palindrome Check: Write a program to check if a number entered by the user is a palindrome using a while loop.

"""


n=int(input("Enter the number"))

origrnal_num= n

reverse=0

while n>0:
    digit=n%10
    
    reverse=reverse*10+digit
    
    n//=10
    
if origrnal_num == reverse:
    print("The number is a palidrome")    
else:
    print("No it is not palidrome")