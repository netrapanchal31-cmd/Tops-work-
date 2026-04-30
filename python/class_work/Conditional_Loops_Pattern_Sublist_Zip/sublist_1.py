


lst1=[1,2,3]
lst2=[1,2,3,[3,4]]

for i in lst2:
    if type(i) == list:
        print("List contains sublist")
        break
else:
    print("List doesnt contains sublist")
       
        