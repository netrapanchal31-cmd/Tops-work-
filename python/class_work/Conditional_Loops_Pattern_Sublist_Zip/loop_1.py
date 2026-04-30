#list for 
lst_number=[1,45,67,89,90,12]
print(lst_number)
sum=0
for i in lst_number:
    sum=sum+i
    print(i)

print(f'sum={sum}')

lst_names=['mahek', 'netra', 'krish', 'lata','neel']
print(f"length of list{len(lst_names)}")
for i in lst_names:
    print(i)
    print(f"length of {i} is {len(i)}")