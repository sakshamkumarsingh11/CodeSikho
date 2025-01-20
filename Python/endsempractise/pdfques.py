"""Write a function lessthan(lst, k) to return list of 
numbers less than k from a list lst. The function must 
use list comprehension."""
"""def lessthan(lst, k):
    return [x for x in lst if x < k]

# Example usage
numbers = [10, 5, 20, 15, 3, 8]
k = 10
print(lessthan(numbers, k))  # Output: [5, 3, 8]"""






"""Write a Python function removekth(s, k) that takes as input a
string s and an integer k>=0 and removes the character at index 
k. If k is beyond the length of s, the whole of s is returned"""

"""def remove_index(s,k):
    if k<0 or k>=len(s):
        return s
    return s[:k]+s[k+1:]    
print(remove_index("Hellopython",8))"""


"""Write a program to find the number of instances of
different digits in a given number."""


def count_digit(number):
    num_str=str(abs(number))            #make it positive
    storage_set={}
    
    for digits in set(num_str):
        storage_set[digits]=num_str.count(digits)
    return storage_set


num=int(input())
print(count_digit(num))