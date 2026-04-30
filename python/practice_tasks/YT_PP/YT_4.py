#WAP to find the greatest of 3 number entered by the user 
first=int(input("Enter first: "))
second=int(input("Enter second: "))
third=int(input("Enter third: "))
if first>second and first>third:
    print("The greatest number is first")
elif second>third:
    print("The greatest number is second")
else:
    print("The greatest number is third")