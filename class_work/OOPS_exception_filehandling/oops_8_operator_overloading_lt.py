class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        print(f"{self.x}-{self.y}")
    def __le__(self,other):
        p3=point(0,0)
        p3.x=self.x<=other.x
        p3.y=self.y<=other.y
        return p3


p1=point(2,45)
p2=point(4,21)
p1.display()
p2.display()
p3=p1<=p2

p3.display()

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def display(self):
        print(f"{self.x}-{self.y}")
    def __ne__(self,other):
        p3=point(0,0)
        p3.x=self.x!=other.x
        p3.y=self.y!=other.y
        return p3


p1=point(2,45)
p2=point(2,65)
p1.display()
p2.display()
p3=p1!=p2

p3.display()