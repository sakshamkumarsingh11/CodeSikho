d={"name":"Saksham", "age":"17", "city": "ghaziabad"}

print(d)
print(d["name"])
print(d.get("age"))

#2 ways to exxcess them

d["age"]=15
print(d)
#updation

d["Height"]="180cm"
print(d)                        #adding key and value


d.pop("age")
print (d)                        #poping out keys and values

print(d.clear)                   # clear

#Iteration of dictionaries 

d={"name":"Saksham", "age":"17", "city": "ghaziabad"}
for  value in  d:
    print(value)   
for  key in d:
    print(key)
    
for key, value in d.items():
    print(f"{key}: {value}")
    
    
    
#Converting list to dictinories

key=[1,2,3,4,5]
value=[2,3,4,5,6]
print(dict(zip(key,value)))