#Find maximum number using ternary operator.
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and b>c:
    print("The greatest number is ", a)
elif b>c:
    print("The greatest number is ",b)
else:
    print("The greatest number is ",c)