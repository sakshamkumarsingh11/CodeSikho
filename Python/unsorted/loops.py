"""count=0
while count <= 10 :
    print("hello")
    count += 1
 """
 
for i in range(3, 0, -1):  # Outer loop starting from 3 down to 1
    for j in range(i, 0, -1):  # Inner loop printing numbers from i down to 1
        print(j, end="")  # Print numbers in a single line
    print() 