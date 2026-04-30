#default argument
def greet(name="Cutie"):
    print("Good Morning ",name)

def square(no=1):
    return no*no

#calling
greet()
greet("Netra")
ans=square()
ans2=square(2)
print(ans)
print(ans2)