#Write a program to write series 1/1! + 1/2! + 1/3! + 1/4! ....1/number!
num=int(input("Enter a number: "))
fact=1
sum=0
for i in range(1,num+1):
    fact=i*1
    sum=sum+(1/fact)
print("the series of number", sum)


