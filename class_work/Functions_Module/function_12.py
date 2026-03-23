#create a function called addition
def addition(*add):
  total=0
  for i in add:
    total+=i
  return total
    

print(addition(1,2,3))
print(addition(11,22))
print(addition(45,56,89,98,87))

#average 
def average(*args):
  avg=sum(args)/len(args)
  return avg


print(addition(1,2,3), average(32,34,53))
print(addition(11,22),average(12,34,52,52))
print(addition(45,56,89,98,87), average(26,32,4,2,32))
