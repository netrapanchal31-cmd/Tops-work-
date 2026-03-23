#Write a program to display number names of entered number e.g number="345" output = Three Four Five
number=input("Enter number: ")
Digit={0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
 
for i in number:
    num=int(i)
    print(Digit[num], end=" ")

