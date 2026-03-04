a=int(input("enter first number :"))
b=int(input("enter secound number :"))
c=int(input("enter third number :"))
if (a>=b)and(b>=c):
    print(a,"is largest number")
elif (b>=a)and(b>=c):
    print(b,"is largest number")
else:
    print(c,"is largest number")