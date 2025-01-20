"""Write a program to simulate the FizzBuzz problem:

Print numbers from 1 to 100.
If a number is divisible by 3, print "Fizz."
If divisible by 5, print "Buzz."
If divisible by both 3 and 5, print "FizzBuzz."""

for i in range(1,101):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)