"""f=open("file.txt", "r" )
data=f.read()
print(data)
f.close()
"""


f=open("file.txt", "r" )
data=f.read(15)          #just prints starting 15 characters
print(data)
f.close()


f=open("file.txt", "r")

data=f.read()
print (data)                    # ab the pointer will read the whole file  till end


line1=f.readline()      #this will not read any further line as sari lines pointer pehle hi read kar chuka hai
# but agar sirf readlines dalte toh voh lines read krta 
