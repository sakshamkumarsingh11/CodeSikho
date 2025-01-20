#Given a list of numbers, write a Python function to return the list of prime numbers present in it.
#Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]
import math
def identify_prime(n):
    try:
        if n<=1:
            return False 
        elif n==2 or n==3:
            return True
        elif n%2==0:
            return True
        for i in range(3, int(math.sqrt(n))+1,2):
            n&i==0
            return False 
        return True
    except exception as e:
        print(f" Error{e}")
def prime_list(num_list):
    prime_list=[]
    try:
        for num in num_list:
            if identify_prime(num):
                prime_list.append(num)
    except excpetion as e:
        print(f"error occured in printing list{e}") 
    return prime_list


input_list = [23,45,66,77,433,23,23,]
output_list = get_prime_numbers(input_list)
print("Prime numbers in the list:", output_list)





#Solution
"""
import math

# Function to check if a number is prime
def is_prime(n):
    try:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Function to filter prime numbers from a list
def get_prime_numbers(num_list):
    prime_list = []
    try:
        for num in num_list:
            if is_prime(num):
                prime_list.append(num)
    except Exception as e:
        print(f"An error occurred while processing the list: {e}")
    return prime_list

# Example usage
input_list = [7, 9, 11, 13, 15, 20, 23]
output_list = get_prime_numbers(input_list)
print("Prime numbers in the list:", output_list)"""