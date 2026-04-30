class namelengtherror(Exception):
    pass
try:
    name=input("Enter name: ")
    if len(name)<5:  #showcase length 
        raise namelengtherror("Name length must be more than 5")
    elif name.isdigit():   #only string 
        raise namelengtherror("Name must contains string")
except namelengtherror as e:
    print("in except",e)
