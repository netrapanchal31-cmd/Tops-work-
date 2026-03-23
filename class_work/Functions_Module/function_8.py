#create to check whether the number is odd or even 
def OE(number):
    if number%2==0:
        return "EVEN"
    else:
        return "ODD"

def iseven(no):
    return no%2==0
#calling

ans= OE(33)
print(ans)
print(OE(44),iseven(44))
print(OE(65),iseven(65))
