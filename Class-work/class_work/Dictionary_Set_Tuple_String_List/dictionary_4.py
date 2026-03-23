# one key multiple value
dic1={"riya@gamil.com":['riya',20,'cgroad',230], "netrapanchal@gamil.com":['netra',20,'ranip',190] }
for k,v in dic1.items():
    print(k,v)
for i in dic1.values():
    print(i)
#fetch value from keys
print(dic1["netrapanchal@gamil.com"])
#print marks more than 120
print(i[3])
sum=0
for i in dic1.values():
   if i[3]>150:            
     print(i)               
#add total marks

   sum+=i[3]
print(sum)
