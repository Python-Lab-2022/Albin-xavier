fn=open("txt5.txt","r")
fn1=open("t3.txt","w")
content=fn.readlines()
print("content\n",content)
for i in range(0,len(content)):
    if(i%2==0):
        fn1.write(content[i])
    else:
        pass
fn1.close()
fn1=open("txt5.txt","r")
cont1=fn1.read()
print("\n odd lines \n",cont1)
fn.close()
fn1.close()
