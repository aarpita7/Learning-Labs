# OOPs (Object oriented programming)
# A programming that solving a problem by creating object.

# Class and Object
'''
-- A class is a blueprint for creating objects.
-- It defines the attributes and methods that objects of that class will have. 
-- An object is an instance of a class.
-- and it represents a specific entity with unique attributes.
'''

class Family:
    pass  # empty class 

n = Family()


# Data members in class
# Instance Variable
'''
-- Instance variables are attributes that are specific to each instance (object) of a class. 
-- These variables store data related to that particular instance.
-- and can have different values for different instances of the same class.
'''
class Family:
    pass  # empty class 

n = Family() # instance variable

# Class Variable
'''
-- Class variables are variables that are shared among all instances of a class.
-- Unlike instance variables, which are unique to each object.
-- class variables are common to all objects of the same class.
'''
class Family:
    classvar=0 # class variable
n = Family()

# Methods in class
'''
-- also known as instance methods.
-- these methods have access to the instance data through the self parameter.
'''
# Data encapsulation
'''
-- Encapsulation is the bundling data and methods within a class.
-- It helps in hiding the internal implementation details of an object from the outside world.
'''

# Data Abstraction
'''
-- exposing only the essential features of an object to the outside world.
'''
class Family:
    def __init__(self,name,age,lname):
        self.name = name
        self.age = age
        self.lname= lname
    

    def getlastname(self):
        return self.lname
    
    def setlastname(self,lname ):
        if lname =='Mahapatra':
            print("Found!")
        else:
            print("Not found!")
family1 = Family("Arpita",18,'Mahapatra')

print(Family.getlastname())

print(Family.getlastname())

# Data Hiding
'''
-- Data hiding is a technique used to prevent direct access to an object's internal data from outside the class.
'''
class MyClass:
    def __init__(self):
        self.__hidden_var = 0 

    def gethvar(self):
        return self.__hidden_var

    def sethvar(self, value):
        self.__hidden_var = value

obj = MyClass()

obj.sethvar(40)

print(obj.gethvar())

# Inheritance
'''
-- way of creating a new class for using details of an existing class without modifying it.
'''

class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")


class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")


dog1 = Dog()
dog1.eat()
dog1.sleep()
dog1.bark()

