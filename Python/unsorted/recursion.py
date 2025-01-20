#factorial with recurrsion 
"""def fact(n):
    if (n==0 or n==1):
        return 1
    return fact(n-1)*n
print(fact(4))"""



# to find the sum of n natural numbers
"""
def cal_sum(n):
    if (n==0):
        return 0
    return cal_sum(n-1)+n

sum=cal_sum(10)

print(sum)"""

def print_list(list,idx=0):
    if(idx== len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits=["apple", "banana", "gauva", "melon"]
print_list(fruits)