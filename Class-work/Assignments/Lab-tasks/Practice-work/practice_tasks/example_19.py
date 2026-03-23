#	Write a program to display numbers which are divisible by 13 from given range.
first_num=int(input("Enter a number: "))
second_num=int(input("Enter a second number: "))
for i in range(first_num,second_num+1):
    if i%13==0:
        print("Divisible of 13=",i )