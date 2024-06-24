class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price
    

    def set_data(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price
    

    def display_data(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Volume: {self.engine_volume} L")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_manufacturer(self):
        return self.manufacturer
    
    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_engine_volume(self):
        return self.engine_volume
    
    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price


car = Car("Model S", 2022, "Tesla", 3.0, "Red", 79999)
car.display_data()

print("\nUpdating car data...\n")
car.set_data("Model 3", 2021, "Tesla", 2.5, "Blue", 59999)
car.display_data()

print("\nAccessing individual fields...\n")
print(f"Model: {car.get_model()}")
print(f"Year: {car.get_year()}")
print(f"Manufacturer: {car.get_manufacturer()}")
print(f"Engine Volume: {car.get_engine_volume()} L")
print(f"Color: {car.get_color()}")
print(f"Price: ${car.get_price()}")
