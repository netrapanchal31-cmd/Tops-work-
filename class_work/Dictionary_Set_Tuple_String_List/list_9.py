city=['ahmedabad','surat','baroda']

ans=[i.upper() for i in city]
print(ans)
ans2=[len(i) for i in city]
print(ans2)

# square of element is even
number=[1,2,3,4,5,6,7,8,9,9]
for i in number:
    if i%2==0:
        number.append(i**2)
print("square of even number", number)

number6=[i**2 for i in number if i%2==0]
print(number6)

