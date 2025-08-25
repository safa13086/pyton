a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if (a>b) and (a>c):
    print("A is greater",a)
elif (b>a) and (a>c):
    print("B is greater",b)
else:
    print("C is greater",c)
