import re

msg="this is python class"
ans=re.findall(r"\b\w{4}\b",msg)
print(ans)
ans=re.findall(r"\w+",msg)
print(ans)