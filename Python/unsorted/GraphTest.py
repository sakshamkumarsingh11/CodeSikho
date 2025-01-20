name = "Saksham"  

for i in range(3):
    print(" " * 10 + "@@@" + " " * 20 + "HAPPY DIWALI")

print(" " * 9 + "====" + " " * 19)
print(" " * 8 + "/    \\" + " " * 18 + " Saksham Kumar Singh, S24CSEU2425")
print(" " * 7 + "/******\\" + " " * 17)

n = 5
for i in range(1, n + 1):
    print("*" * (7 - i) + "/" + "~" * (2 * i + 6) +"\\***********")


for i in range(3):
    if i == 1:  
        print(" "*2 + "|" + name.center(16) + "|")
    else:
       print(" " * 2 + "|---* * * * *----|")


for i in range(n, 0, -1):
    print(" " * (7 - i) + "\\" + "~" * (2 * i + 6) + "/")

print("*" * 7 + "\\------/")
print("*" * 8 + "\\____/")


for i in range(3):
    print("*" * 10 + "|")