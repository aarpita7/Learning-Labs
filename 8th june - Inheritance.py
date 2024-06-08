# Inheritance 
'''
-- Inheritance provides code reusability to the program 
-- because we can use an existing class to create a new class instead of creating it from scratch.
-- the child class acquires the properties 
-- and can access all the data members and functions defined in the parent class.
'''
class ParentClass:
    def parent(self):
        print("This parent class")

class ChildClass(ParentClass):
    def child(self):
        print("This is child class")

# MRO (Method Resolution Order)
'''
-- a set of rules that define the order in which Python searches for methods 
-- when dealing with class inheritance
'''
class Vehicle:
  def identify(self):
    print("I am a vehicle")

class Car(Vehicle):
  def identify(self):
    print("I am a car")

class ElectricVehicle(Vehicle):
  def identify(self):
    print("I am an electric vehicle")

class HybridCar(Car, ElectricVehicle):
  pass 

hybrid = HybridCar()
hybrid.identify()


# Single Inheritance 
class Vehicle:
  def identify(self):
    print("I am a vehicle")

class Car(Vehicle):
  def __init__(self, model):
    self.model = model

  def identify(self):
    print(f"It's {self.model} car")

car = Car("Sedan")
car.identify()  # Output: It's Sedan car


# Multiple Inheritance 
class Engine:
  def start(self):
    print("Engine started")

class Battery:
  def charge(self):
    print("Battery charged")

class ElectricCar(Engine, Battery):
  pass


electric_car = ElectricCar()
electric_car.start()  # Output: Engine started (from Engine)
electric_car.charge()  # Output: Battery charged (from Battery)


# Hierarchical Inheritance
class Shape:
  def draw(self):
    print("Drawing a shape")

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def draw(self):
    print(f"Drawing a circle with radius {self.radius}")

circle = Circle(5)
circle.draw()  # Output: Drawing a circle with radius 5


# Method Overriding
'''
-- is an ability that allows a subclass or child class to provide a specific implementation of a method
-- that is already provided by one of its super-classes or parent classes.
'''
class Animal:
  def make_sound(self):
    print("Generic Animal Sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")

class Cat(Animal):
  def make_sound(self):

    print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!

# Super() Method
class Animal:
  def make_sound(self):
    print("Generic Animal Sound")

class Dog(Animal):
  def make_sound(self):
    print("Woof!")
    super().make_sound() 

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Woof! (from Dog), Generic Animal Sound (from Animal)
cat.make_sound()  # Output: Meow! (from Cat)

