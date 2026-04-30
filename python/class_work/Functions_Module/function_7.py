#square of list 
def spuare(number):
    return number*number

#calling
lst_sq=[]
lst_no=[11,23,234,21,3]
for i in lst_no:
    print(spuare(lst_no))
    print(lst_sq.append(spuare))

print(lst_sq)
