#search for a number x in this tuple using loop 
#[1,4,9,16,25,36,49,64,81,100]
num=(1,4,9,16,25,36,49,64,81,100)
user_x=int(input("Enter the searching number: "))
i=0
while i<len(num):
    if(num[i]==user_x):
        print("Found at index",i)
    else:
        print("NOT Found again")

    i+=1

print("END")
