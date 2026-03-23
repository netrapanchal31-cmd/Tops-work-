#WAP to enter marks of 3 subjects from the user and store that in dictionary. start with empty one and end up by one by one. 
#subj as key and marks as value 
marks={}
sub1=int(input("Enter english marks: "))
marks.update({"English " : sub1})
sub2=int(input("Enter maths marks: "))
marks.update({"Maths " : sub2})
sub3=int(input("Enter economy marks: "))
marks.update({"Economy " : sub3})
sub4=int(input("Enter hr marks: "))
marks.update({"HR " : sub4})
sub5=int(input("Enter marketing marks: "))
marks.update({"Marketing " : sub5})

print(marks)