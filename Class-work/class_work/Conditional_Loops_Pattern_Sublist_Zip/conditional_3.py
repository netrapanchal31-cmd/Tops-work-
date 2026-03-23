# nested if 

age=int(input("enter your age"))
weight=int(input("enter your weight"))
if age>18:
    if weight>50:
        print("user is eligiable to donate blood")
    else:
        print("due to under weight user cannot donate blood")
else:
    print("due to under age user cannot donate blood")


# users eligiablity 

age=int(input("enter your age"))
ll=input("do you have learning licence?")
if age>18:
    if ll in ("yes", "YES", "Yes"):
        print("user is eligiable for licence")
    else:
        print("dont have learning licence")
else:
    print("under age")