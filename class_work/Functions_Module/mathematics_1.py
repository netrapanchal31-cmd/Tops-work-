def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def isEven(num):
    if num%2==0:
        return True
    else:
        return False

def countDigit(num):
    count=0
    while(num!=0):
        rem=num%10
        count+=1
        num=num//10
    return count

 

        