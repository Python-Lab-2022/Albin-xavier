num=int(input("enter the number:"))
a=1
if num<0:
    print("factorial does not exist for negative numbers")
elif num==0:
    print("factorial for 0 is 1")
else:
    for i in range (1,num+1):
        a=a*i
    print(a)
    
