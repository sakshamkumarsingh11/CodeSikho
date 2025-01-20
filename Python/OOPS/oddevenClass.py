class Number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)

n1=Number(11)
n2=Number(29)        
n3=Number(24)
n4=Number(2)
n5=Number(17)
n6=Number(19)


print ("All the even numbers are: ", Number.even)
print ("All the odd numbers are: ", Number.odd)


