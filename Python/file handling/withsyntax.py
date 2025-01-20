word= "understand"
with open("practice.txt", "r") as f:
    data = f.read()
neww_data= data.replace("python", "go")                 #using replace
print(neww_data)
    
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word)!=0):
        print("found")
    else:
        print("Not found")