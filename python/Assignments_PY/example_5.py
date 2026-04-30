#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).  
#If the given string already ends with 'ing' then add 'ly' instead If the string length of the given  
#string is less than 3, leave it unchanged 

word=input("enter word: ")
if len(word)<3:
    print(word)
else:
    if word.endswith("ing"):
        print(word+"ly")
    else:
        print(word+"ing")