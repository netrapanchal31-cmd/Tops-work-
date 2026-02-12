#month to outcome as days

month=input("Enter a month")
if month in ("january" , "march" , "may" , "july" , "august" , "october" , "december" ):
    print("days=31")
elif month in ("febuary"):
    print("days=28/29")
elif month in ("april", "june", "september", "november"):
    print("days=30")
else:
    print("invalid month")

#leap or not 

year=int(input("enter a year"))
if year%4==0 and year%100!=0 or year%400==0:
    print(f"{year} it is a leap year")
else:
    print(f"{year} it is not a leap year")








