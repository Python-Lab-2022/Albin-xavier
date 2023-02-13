list=[]
list1=[]
l=int(input("enter lower range"))
u=int(input("enter the upper range"))
if l<=999 or u>=9999:
    print("plese enter a 4 digit number:")
else:
    for i in range(l,u):
        list.append(i)
    for i in list:
        if i**0.5==int(i**0.5):
               list1.append(i)
print(list1) 
    
    


