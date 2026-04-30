import re

msg="Contact number is 3456874356 and pincode is 23672"
ans=re.findall(r"\d{6,10}",msg)
ans=re.findall(r"\d+",msg)
print(ans)
