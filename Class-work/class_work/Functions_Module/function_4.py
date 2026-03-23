#creat a function to perform addition with written function 
def addition(no1,no2):
    return no1+no2
     
def substration(no1,no2):
   print("substraction is-->",no1-no2)
  

#calling
i=int(input("enter no1 "))
i2=int(input("enter no2 "))
Ans=addition(i,i2)
print("addition is-->",Ans)
if Ans>=100:
    substration(i,i2)
