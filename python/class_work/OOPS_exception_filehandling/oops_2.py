class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def drive(self):
        print(f"{self.brand}--{self.speed}")
    
obj=car("BMW",200)
obj1=car("MARUTI",100)
obj.drive()
obj1.drive()