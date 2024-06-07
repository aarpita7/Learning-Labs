# Functions
'''
-- enable code reusability, as they can be called multiple times from different parts of a program
-- allow developers to break down complex tasks into smaller
''' 
def greet(name): #Function definition with parameter 'name'
    #This function prints a greeting message.
    print("Hello", name + "!")

# Function call with argument 'Arpita'
greet("Arpita")

# Positional Arguments
#arguments passed to the function in the same order they are defined in the function declaration. 
def carea(length, width):
  return length * width

# Calling the function with positional arguments
area = carea(5, 3)  # length = 5, width = 3
print(area)  # Output: 15

#Keyword Arguments
''' 
-- passed by name when calling the function. 
-- The order doesn't matter as long as you associate the value with the correct parameter name.'''
def greet(n, m="Hello"):
  print(m, n + "!")

# Calling with keyword arguments (notice order is switched)
greet(m="Hi", n="Arpita")  # Output: Hi Arpita

# Default Arguments
'''
-- arguments have pre-defined values assigned within the function definition. 
-- If no value is passed during the function call, the default value is used.
'''
def greet(name="World"):
  print("Hello", name + "!")

# Calling with default argument
greet()  # Output: Hello World!

# Calling with a custom argument
greet("Arpita")  # Output: Hello Arpita!


# Variable Length Arguments (args):
'''
--This allows a function to accept an arbitrary number of positional arguments.
--These arguments are packed into a tuple inside the function.
'''
# Keyword Variable Length Arguments (kwargs):
'''
-- these arguments are captured in a dictionary. 
-- therefore they are accessible as key-value pairs within the function.
'''

# Keyword-Only Arguments
'''
-- arguments must be preceded by * in the function definition. 
-- They can only be passed by keyword name, not by position.
'''

# Passing Function as arguments
'''
-- functions are first-class objects, can be treated like any other data type. 
-- This allows you to pass functions as arguments to other functions. 
-- often referred to as higher-order functions. 
'''
def shout(text):
  return text.upper()

def whisper(text):
  return text.lower()

def modify_text(text, func):
  return func(text)

yelled_text = modify_text("Hello arpita!", shout)
print(yelled_text)  # Output: HELLO ARPITA!

whispered_text = modify_text("HELLO ARPITA!", whisper)
print(whispered_text)  # Output: hello arpita!


# Lambda Function
'''
-- Lambda functions lack a formal name, hence the term "anonymous."
-- They are defined using the lambda keyword followed by arguments, a colon, and the expression to be evaluated.
-- It is a single lined function 
'''
# int
add = lambda x, y: x + y

result = add(7, 3)
print(result)  # Output: 10

# string
greeting = lambda name: f"Hello, {name}!"

print(greeting("Arpita"))  # Output: Hello, Arpita!


# Map, Reduce and Filter
'''
Map- The map function applies a given function to all elements of an iterable (like a list) 
   - returns an iterator containing the transformed elements.

Reduce- reduce applies a function cumulatively to all elements of an iterable, reducing it to a single value.

Filter- The filter function creates a new iterator containing elements from an iterable that pass a test condition.
'''

# Local and Global Variable
#  Local variable
''' 
Local variables are created within a function definition.
They are only accessible within that function and its nested functions.
When the function finishes execution, local variables are destroyed.
'''
# Global variable 
'''
Global variables are declared outside of any function definition.
They are accessible throughout the program, by any function.
'''

#Variable scope 
'''
Variable scope defines the areas of your code where a variable can be accessed. 
Python follows the LEGB (Local, - Enclosed, Global, Built-in) rule for scoping:

Local (L): Variables defined within a function (including parameters).
Enclosed (E): Variables defined in enclosing functions (nested functions).
Global (G): Variables declared outside all functions in the current module.
Built-in (B): Built-in functions and variables defined within Python itself.
'''

x = 10  # Global variable

def myfunc():
  y = 20  # Local variable
  print("Inside function:", x, y) 

  def ifunc():
    z = 30  # Local variable
    print("Inside inner function:", x, y, z)  

  ifunc()

print("Outside function:", x) 

myfunc()


