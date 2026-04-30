lst=[1,2,3,4]
lst_sq=(i*i for i in lst)
print(lst_sq)

print(lst_sq.__next__())
print(lst_sq.__next__())
print(lst_sq.__next__())