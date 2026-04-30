#Write a python program using function to find  the sum of odd series and even series 
#Odd series:  12/ 1!  +   32/ 3!   +  52/ 5!+……n  
#Even series: 22/ 2!  +   42/ 4!   +  62/ 6!+……n
import math
start_no=int(input("Enter a start number: "))
odd_even=input("Even/odd? ")
num_iteration=int(input("Enter a range: "))
j=2
ans1=0
if odd_even=="Even":
    j=2
else:
    j=1
for  i in range(0,num_iteration):
    print(start_no,"-",j,"-",math.factorial(j))

    ans=start_no/math.factorial(j)
    print(ans)
    ans1+=ans
    j+=2
    start_no+=20

print(ans1)