import re
lst_eamil=["test@gmail.com","test3425@gmail.com","test@gmail.com","test_554@gmail.com"]
pattern= r"^\w+@\w+\.\w+$"
for i in lst_eamil:
    ans=re.search(pattern,i)
    print(ans)