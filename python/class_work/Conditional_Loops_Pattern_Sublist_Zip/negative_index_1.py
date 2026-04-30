name=input("enter name")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])


#string slicing = using start and end 
print(name[0:5])
#print from 5 to 9=using start and end
print(name[5:10])
#print alternative = using step 
print(name[2:11:2])
#print letter upto 7= end 
print(name[:7])
#print alternate letters upto 7= end and step
print(name[:7:2])
#print string from letter 5= only start 
print(name[5:])
#str1=name[:5]

print(name[-2:]) #backward 2 words from last 
print(name[:-2]) #print whole 
#reverse 
print(name[::-1])

# swip
name2=input("enter a name")
ans= name2[-1] + name2[1:len(name2)-1] + name2[0]
print(ans)