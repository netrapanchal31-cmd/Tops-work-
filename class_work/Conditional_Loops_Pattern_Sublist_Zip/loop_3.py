#factorial of given number 
num=int(input("enter a number"))
mul=1
#(num,1)------------- (num,0,-1)
for i in range(1,num+1):
    mul=mul*1

print(f"factorial of {num} is {mul}")


      