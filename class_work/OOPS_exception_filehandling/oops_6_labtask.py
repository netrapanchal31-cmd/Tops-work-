#inheritance type
#single ineritance 
class parents:
    def greet(self):
        print("good morning")
        
class child(parents):
    def greet(self):
        print("good morning from child")

obj=parents()
obj1=child()
obj.greet()
obj1.greet()
        
#multiple inheritance
class parent1:
    def greet(self):
        print("good morning from parent1")

class parent2:
    def greet(self):
        print("good morning from parent2")

class child(parent1,parent2):
    def greet(self):
        print("good morning from child")

obj=parent1()
obj1=parent2()
obj2=child()
obj.greet()
obj1.greet()
obj2.greet()
        

        
        