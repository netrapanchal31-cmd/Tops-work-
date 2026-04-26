def Evennumber(num):
    if num%2==0:
        return num 
    

lst_1=[1,2,33,42,41,53]
even_lst=list(filter(Evennumber,lst_1))
print(even_lst)