# Assignment 1: Design Your Own Class! 🏗️

# Base class Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        # Attributes
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in mAh

    # Method to show details
    def show_info(self):
        print(f"📱 {self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}mAh")

    # Method to simulate charging
    def charge(self):
        print(f"{self.brand} {self.model} is charging 🔋...")

# Subclass GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        # Call parent constructor
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system  # extra attribute

    # Overriding method (polymorphism)
    def show_info(self):
        print(f"🎮 {self.brand} {self.model} | {self.storage}GB | {self.battery}mAh | Cooling: {self.cooling_system}")

    # New method specific to gaming phones
    def start_game_mode(self):
        print(f"{self.brand} {self.model} is now in Gaming Mode 🚀🔥")

# Create objects
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, 6000, "Liquid Cooling")

# Demonstrate methods
phone1.show_info()
phone1.charge()

phone2.show_info()
phone2.charge()
phone2.start_game_mode()



# Activity 2: Polymorphism Challenge! 🎭

class Vehicle:
    def move(self):
        print("This vehicle moves in some way.")

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("⛵ Sailing on water.")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each calls its own move() definition
