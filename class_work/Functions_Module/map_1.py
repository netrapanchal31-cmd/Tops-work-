def square(n):
    return n*n

#lambad
lst_lam=list(map(lambda num:num*num))


lst_no=[1,2,33,54,53]

lst_sq=list(map(square,lst_no))
print(lst_sq)

lst_city=["ahmedaba","surat","baroda"]
upper_city=list(map(str.upper,lst_city))
print(upper_city)

lst_base=[1,2,4,5,6]
lst_power=[1,2,2,1]
lst_ans=list(map(pow,lst_base,lst_power))
print(lst_ans)