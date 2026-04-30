import re
name="Netra"
ans=re.search(r"t",name)
print(ans)
if ans:
    print(f"found at {ans.start()}")
else:
    print("not found")