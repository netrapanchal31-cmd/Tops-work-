#sumof square of all even number 
from functools import reduce
def evennumber(num):
    if num%2==0:
        return num 
    
lst=[2,32,2,4,3,4,45,54]
num1=list(filter(evennumber,lst))
even_no=list(map(lambda num:num*num,lst))
ans=reduce(lambda x,y:x+y,even_no)
print(ans)

#with single line 
ans1=reduce(lambda x,y:x+y,list(map(lambda num:num*num,list(filter(evennumber,lst,)))))
print(ans1)

