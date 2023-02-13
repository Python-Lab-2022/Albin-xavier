list=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    list.append(int(input()))
print(list)
total=sum(list)
print("sum of all elements in given list is:",total)
    
