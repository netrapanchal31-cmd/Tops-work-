#Print no. of days in given list of Months 
# e.g ['April','February','May'] output April - 30 Days February - 28 or 29 days,May 31 Days
month=input("Enter a month: ").lower()
# month.lower()
if month in ("january","march","may","july", "august", "october","december"):
    # month.upper()
    print("days=31")
elif month in ("april","june","september","november",):
    # month.upper()
    print("days=30")
elif month in ("february"):
   
    print("days=28/29")
else:
    print("Invalid month")


