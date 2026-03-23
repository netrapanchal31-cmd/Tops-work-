#recreate avg function as now while calling avg function   ignoring string   avg=(1,2,"netra",3)=       3 avg==6/3
def addition(*add):

  
  total=0
  for i in add:
   if type(i)==int:
    total+=i
    
  return total

def average(*args):
    total1=0
    for i in args:
        if type(i)==int:
            total1+=1
        avg=sum(args)/int(len(args))
    return avg

ans=(addition(1,2,3,"netra"),average(1,2,4,67,"netra"))
print(ans)





