#variable arguments/ different arguments 
def student_details(*args):    #args is a variable 
    print(args) #normal
    print(end="\n\n")   #new line
    for i in args:
        print(i,end="\t") #one by one

student_details("netra",20,"com")
student_details("krish",22,"com","ahm")
student_details("lata",21,"com","ahm","lata@gamil.com")


