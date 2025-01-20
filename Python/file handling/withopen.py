with open ("demo.txt", "r") as f:
    data=f.read()
    print(data)
    
with open("demo.txt","w") as f:
    f.write("Hello now this is the new part of data i created to learn about  write mode in with syntax")
    