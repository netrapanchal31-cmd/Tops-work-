num=int(input("enter a number"))
temp=0
for i in range(2,num):
    if num%i==0:
        print("not a prime number")
        temp=1
        break
    else:
        temp=0
if temp==0:
    print("it is prime number")
        