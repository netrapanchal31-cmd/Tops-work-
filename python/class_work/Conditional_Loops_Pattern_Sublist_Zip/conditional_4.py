marks=int(input("enter marks"))
if marks>=70 and marks<=100:
    print("A")
elif marks>=60 and marks<=69:
    print("B")
elif marks>=40 and marks<=59:
    print("C")
elif marks>=35 and marks<=39:
    print("PASS")

match marks:
    case m if 70<= m <=100: print("A")
    case m if 69<= m <=60: print("B")
    case m if 40<= m <=59: print("C")
    case m if 35<= m <=39: print("PASS")
    case _:print("INVAILD MARKS")