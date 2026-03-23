#write a Python program to check whether a list contains a sublist. 
lst_name=("netra","krish","lata")
lst_name2=("netra","lata",["krish","neha","neel"])

for i in lst_name2:
    if type(i)==list:
        print("List contains a sublist-->")
        break
else:
        print("List doesnot contains a sublist-->")
        