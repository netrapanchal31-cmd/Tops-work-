#Print no of digits and letters in String.Accept String from user. E.g string="H1Visa" Digits = 1 and letters=5
i=input("Enter a string: ")
Digit=0
letter=0
for m in i:
    if m.isdigit():
      Digit+=1
    elif m.isalpha():
        letter+=1
print("Digits: ",Digit)
print("Letters: ",letter)

    