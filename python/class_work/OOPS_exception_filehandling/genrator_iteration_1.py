#special kind of function whenever required lazly.== generator it generate items one at a time only when it is a needed using functions they help to save memories to working large data set 
#yield vs return ..................yeild= pause 
def my_generator():
    for i in range (6):
        yield i   #generatr object  pause and go back

ans= my_generator()
# print(ans)

# for i in ans:
#     print(i)


print(ans.__next__())
print(ans.__next__())
print(ans.__next__())
print(ans.__next__())
