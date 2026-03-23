#Given a number n, write a python program to make and print the list of Fibonacci series up to n. 
#Input : n=7  
#Hint : first 7 numbers in the series 
#Expected output :  
#First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13
n=7
fibonacci=[]
a,b=0,1
for i in range (n+1):
    fibonacci.append(a)
    a,b=b,a+b
print("Fibonacci series", end="= ")
print(*fibonacci,sep=" ")

