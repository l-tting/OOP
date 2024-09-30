class Car:
    def __init__(self,brand,name) :
        self.brand =brand
        self.name= name
    
    def move(self):
        print(f"Drive {self.name}")   

class Boat:
    def __init__(self,name):
        self.name =name
    
    def move(self):
        print(f"Sail {self.name}")

class Plane:
    def __init__(self,name):
        self.name =name
    def move(self):
        print(f"Fly {self.name}")

car = Car("Audi","A3")
boat = Boat("MV9000")
plane = Plane("G550")



for move in(car,boat,plane):
    move = move.move()
print(move)
        