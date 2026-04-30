#Counting the frequencies in a list using a dictionary in Python. 
#Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2] 
#Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2
input=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
dic_1={}
for i in input:
    if i in dic_1:
        dic_1[i]+=1
    else:
        dic_1[i]=1

for key in sorted(dic_1):
    print(f"{key} : {dic_1[key]}")


