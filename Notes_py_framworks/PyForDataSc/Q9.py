# Q9. 9. Demonstrate inheritance using `Vehicle` `Car`.

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    def honk(self):
        print("Honk!")
        
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Toyota", "Corolla")
car.honk()

print(car.brand, car.model)