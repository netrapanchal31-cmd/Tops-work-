#two arguments in function
from functools import reduce 
def add(x,y):
    return x+y

ans=reduce(add,[3,345,2,1,3,5,2,5,2,4,32,5,23,1,5,21])
print(ans)

