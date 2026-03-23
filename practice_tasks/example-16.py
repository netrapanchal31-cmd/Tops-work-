#"Print even numbers fall between 2 given numbers E.g user enter 10 20 
                                   #output 12,14,16,18"
i=int(input("Enter a number: "))
j=int(input("enter a second: "))
for m in range(i,j+1):

    if m%2==0 and m!=10 and m!=20:
        
        print(m)
print("End of the loop")