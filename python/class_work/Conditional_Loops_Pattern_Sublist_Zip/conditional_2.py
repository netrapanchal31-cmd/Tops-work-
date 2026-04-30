age=int(input("enter your age"))
if age>=18:
    print("user is adult")
else:
    print("user is not adult") 

    # num is positive or negative 

no1=int(input("enter a digit"))
if no1>=0:
    print("number is positive")
else:
    print("number is negative")

    # num is odd or even 

number=int(input("enter a number"))
if number%2==0:
    print("even number")
else:
    print("odd number")   

# user enter 
n01=int(input("enter a number"))
if n01%5==0 and n01%7==0:  
    print("it is divided by 5 & 7")
else:
    print("it is not divided by 5 & 7")

# user enter 2 

no2=int(input("enter a number1"))
no3=int(input("enter a number2"))
if no2>no3:  
    print("no2 is greater than no3")
elif no2<no3:
    print("no3 is greater to no2")
else:
    print("no3 is equal no2")


# age entry 

age=int(input("enter your age"))
if age>=0 and age<=2:
    print("infant")
elif age>=3 and age<=18:
    print("minor")
elif age>=19 and age<=50:
    print("adult")
elif age>=51 and age<=70:
    print("senior")
elif age>=71: 
    print("super senior")
else:
    print("age is invalid")

