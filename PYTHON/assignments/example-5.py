word=input("enter word")
if len(word)<3:
    print(word)
else:
    if word.endswith("ing"):
        print(word+"ly")
    else:
        print(word+"ing")