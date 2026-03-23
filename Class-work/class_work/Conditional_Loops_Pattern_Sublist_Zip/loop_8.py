num=int(input("enter number"))
i=1
while i<=10:
    print(f"{num} * {i}= {num*i}")
    i+=1

#leap 
for year in range(1990,2026):
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"{year} year is leap year")
    else:
        print(f"{year} year is not a leap year")

    



