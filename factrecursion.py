x=int(input("enter no.:"))
def fact(x):
    if(x==0):
        return 1
    elif(x<0):
        print("invalid")
    else:
        return x*fact(x-1)
print(fact(x))

