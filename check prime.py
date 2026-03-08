n=int(input("enter number to check prime or not :"))
if n<=1:
    print("invaid number")
else:
    for i in range (2,n):
        if n % i == 0:
            print("it is not a prime number")
            break
    else :
        print("it is prime number")