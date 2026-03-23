#arguments may be more than one but expression is always one
#inline function 
#use for simple calculation not for the complex
#syntax------- lambda argument:expression 
a= lambda x,y:x+y
print(a(12,34))

square=lambda n:n*n
print(square(2))
lst_1=[1,2,3]
lst_2=[]
for i in lst_1:
    lst_2.append(square(i))
print(lst_2)

ans=lambda num:"Even" if num%2==0 else "Odd"
print(ans(45))
for i in lst_1:
    print(ans(i))