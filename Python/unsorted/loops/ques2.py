"""Factorial Calculation: Write a program to find the factorial of a number using a while loop."""

n=int(input("enter input"))

factorial=1

if n<0:
    print("Enter the valid input")

else:
    while n>0: 
        factorial = factorial*n
        n-=1
        print(factorial)