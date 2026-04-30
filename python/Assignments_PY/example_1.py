#Write a python program to sum of the first n positive integers.

number01=int(input("enter a number"))
ans=0
for i in range(1, number01+1):
    ans=ans+i 

print("sum of",number01, "is", ans)


