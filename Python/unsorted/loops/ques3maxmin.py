"""Find Maximum and Minimum: Write a program to find the maximum and minimum value in a list using a for loop.

"""


input_taken=input("Enter input elements")
elements = input_taken.split(",")

l=[int(element) for element in elements]

max_val=l[0]
min_val=l[0]
    
for num in l:
    if num>max_val:
        max_val=num
    elif num<min_val:
        min_val=num

print(f"Max value is {max_val}")    
print(f"Min value is {min_val}")    