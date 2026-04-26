#inheritance 
class person:
    def __init__(self,name,c_no,address):
        self.name=name
        self.c_no=c_no
        self.address=address
    def display(Self):
        print(f"{Self.name}-{Self.c_no}-{Self.address}")

class student(person):
    def __init__(self, name, c_no, address,roll_no,marks):
        super().__init__(name, c_no, address)
        self.roll_no=roll_no
        self.marks=marks
    def displaystudent(self):
        print(f"{self.roll_no}-{self.name}_{self.c_no}-{self.marks}-{self.address}")

class collegestudent(student): #multilevel 
     pass
class company:
    pass
class employee (student,company): #multiple
    pass 

#polymoprism = many forms
#ablity to take more than one form is polymorpism     ex=netra: daughter,sister,friend,student
#2 types
#compile time/static binding---method overloading (same method name, different argument)
#it is not supported by python directly 
#through variable length parameters argument
#operator overloading

# runtime/dynamic binding --- method overriding (same method, same parameter)


obj=student("netra",468433,"ranip",23,250)
obj.displaystudent()

        