class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

   
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_opening_date(self):
        return self.opening_date
    
    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def get_country(self):
        return self.country
    
    def set_country(self, country):
        self.country = country

    def get_city(self):
        return self.city
    
    def set_city(self, city):
        self.city = city

    def get_capacity(self):
        return self.capacity
    
    def set_capacity(self, capacity):
        self.capacity = capacity



stadium = Stadium("Stadium1", "1923-04-28", "asd", "fff", 90000)


print(f"Name: {stadium.get_name()}")
print(f"Opening Date: {stadium.get_opening_date()}")
print(f"Country: {stadium.get_country()}")
print(f"City: {stadium.get_city()}")
print(f"Capacity: {stadium.get_capacity()}")

stadium.set_name("Stadium2")
stadium.set_opening_date("1957-09-24")
stadium.set_country("Ssn")
stadium.set_city("ada")
stadium.set_capacity(99354)


print("\nUpdated stadium data:\n")
print(f"Name: {stadium.get_name()}")
print(f"Opening Date: {stadium.get_opening_date()}")
print(f"Country: {stadium.get_country()}")
print(f"City: {stadium.get_city()}")
print(f"Capacity: {stadium.get_capacity()}")
