#class is blueprint, contains data and function, not real entity 
#object is real entity and it is a type of class 
#data member=name,age............._init_=go give initialition object -calles automatically 
#self=
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def displayperson(self):
        print(f"{self.name}-{self.age}")    
    def greet(self):
        print("Good morning cutie",self.name)
obj=person("netra",20)
#obj.greet()
obj1=person("krish",22)
#obj1.greet()
obj.displayperson()
obj1.displayperson()
netra=person("netra",19)
netra.displayperson()

