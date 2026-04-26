# Multilevel Inheritance    
class grandparents:
    def greet(self):
        print("good morning from grandparents")

class parents(grandparents):
    def greet(self):
        print("good morning from parents")

class child(parents):
    def greet(self):
        print("good morning from child")

obj=grandparents()
obj1=parents()
obj2=child()
obj.greet()
obj1.greet()
obj2.greet()


# Hierarchical Inheritance
class parent:
    def greet(self):
        print("good morning from parent")

class child1(parent):
    def greet(self):
        print("good morning from child1")

class child2(parent):
    def greet(self):
        print("good morning from child2")

obj=parent()
obj1=child1()
obj2=child2()
obj.greet()
obj1.greet()
obj2.greet()

#hybrid inheritance
class A:
    def greet(self):
        print("good morning from A")

class B(A):
    def greet(self):
        print("good morning from B")

class C(A):
    def greet(self):
        print("good morning from C")

class D(B,C):
    def greet(self):
        print("good morning from D")

obj=A()
obj1=B()
obj2=C()
obj3=D()
obj.greet()
obj1.greet()
obj2.greet()
obj3.greet()
    