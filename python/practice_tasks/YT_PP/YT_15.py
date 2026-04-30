#search for a number x in this tuple using loop from list 
lst_1=[1,4,9,16,25,36,49,64,81,100]
x=36
idx=0
for i in lst_1:
    if (i==x):
        print("find",idx)
    idx+=1
  