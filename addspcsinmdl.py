x=input("enter string:")
e=list(x)
if(len(x)%2==0):
    d=int(len(x)/2)
    for i in range(d):
        e.insert(d,"@")
    for i in e:
        print(i,end="")
else:
    e.insert(0,"@")
    e.insert(len(x)+1,"@")
    for i in e:
        print(i,end="")
