statement=input("Enter a statment")
ans=statement.split()
count={}

for i in ans:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
    
print("word counting")
for i in count:
    print(i, " ", count[i])
    