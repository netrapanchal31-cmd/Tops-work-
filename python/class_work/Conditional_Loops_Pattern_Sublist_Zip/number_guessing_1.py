import random
sys_num=random.randint(1,100)

while True:
    user_num=int(input("enter number"))
    if user_num>sys_num:
       print("entered number is greater")
    elif user_num<sys_num:
       print("entered number is lesser")
    else:
     print("you win")

