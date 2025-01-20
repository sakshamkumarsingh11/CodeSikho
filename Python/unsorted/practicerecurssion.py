#ques 1 factorial

"""def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

m=int(input("Enter the number"))
user_input=factorial(m)
print(user_input)
"""



#ques 2 fibonacci

"""def fib(n):
    if n==1 or n==0:
        return 1
    else:
        return fib(n - 1)+fib(n - 2)
m= input("Enter")
m=int(m)
call1 = fib(m)
print(call1)"""

# ques3
# sum of digit


"""def sum(n):
    if n==0:
        return 0
    else:
        return n%10+ sum(n//10)
        
user_input=input("Enter")
user_input=int(user_input)

call=sum(user_input)
print(call)"""


#ques 4 to determine power value

def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)
x=int(input("Enter base:"))
n=int(input("Enter power"))

call = power (x, n)
print(call)

