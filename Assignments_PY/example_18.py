#Python Program to Find Factorial of Number Using Recursion
def factiorial(num):
    if num==0 or num==1:
        return 1 
    else:
        return num*factiorial(num-1)
    
user_int=int(input("Enter a number you want a factorial: "))
print("Factorial of",user_int,"is",factiorial(user_int))