with open("ques.txt","w") as f:
    f.write("Hello i m learning python file handlling and will be testing few models")
    f.write("\npython is a basic language")
    f.write("\nIt is simple to understand")
    
    
with open("ques.txt", "r") as f:
    
    data=f.read()
    
    
with open("ques.txt", "w") as f:
    new_data= data.replace("python", "java")
    print(new_data)