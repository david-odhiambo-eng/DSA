class Car:
    def __init__(self, name: str, brand: str, description: str):
        self.name = name
        self.brand = brand
        self.description = description

    def display_car(self, speed: int):
        print(f'The {self.name} {self.brand} {self.description} has a speed of {speed}')

car: Car = Car(name='AUDI', brand='RS350,', description='which is our latest model')
car.display_car(220)
