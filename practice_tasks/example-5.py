#Find Compond Interest. Amount = P(1 + R/100) t  Compound Interest = A - P
p=float(input("Enter p: "))
r=float(input("Enter r: "))
t=float(input("Enter t: "))
a=p*(1+r/100)**t
print(a)
CI=a-p
print(CI)