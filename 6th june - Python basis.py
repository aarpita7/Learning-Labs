# Python Input and Output Statements

# Input statement
n = input("Enter your name: ")
print("Hello,", n)

# Output statement with keyword arguments
print("Hello", "Arpita", sep=", ", end="\n")

'''The sep keyword argument allows you to specify the separator string 
-- that will be used between the arguments passed to print()'''

# Data Types in Python
'''
int, float, complex are immutable.
str, list, tuple can contain multiple values of different data types.
dict store key-value pairs, where keys must be unique and immutable.
set, frozenset are unordered collections of unique elements.
The bool type represents truth values (True or False).
'''
int_num = 7 # whole numbers
float_num = 2.3 #integers
complex_num = 2 + 3j
string = " Hello! Arpita" # anything inside '' or " "
boolean1= True
boolean2= False
list_example = [2, 3, 7, 23, 74]
tuple_example = (2, 3, 7, 23, 74)
dict_example = {" Name": "Arpita", "age": 18}
set_example = {2, 3, 7, 23, 74}

## Expressions and Operators
a = 7
b = 3

# Arithmetic Operators
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation

# Comparison Operators
print(a == b) # Equal to 
print(a != b) # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b) # Greater than or equal to
print(a <= b) # Less than or equal to

# Logical Operators
print(a > 5 and b < 5)  # and
print(a > 5 or b < 1)   # or
print(not(a > 5 and b < 5)) # not

# operators give output in true or false



# Type Casting
'''
-- Type casting is used to convert data from one type to another.
-- Explicit type conversion is preferred over implicit type conversion.
'''
iff = int(3.14)
ffi = float(10)
sfi = str(100)
lfs = list("Hello")
tfl = tuple([1, 2, 3, 4, 5])
sfl = set([1, 2, 3, 4, 5])

print(iff)
print(ffi)
print(sfi)
print(lfs)
print(tfl)
print(sfl)


# Conditional Statements
'''
Conditions in if, elif, and else statements must evaluate to a boolean value (True or False).
'''
a = 10
b = 5

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")


# Looping Statements

# For loop
'''used to iterate over sequences (like lists, tuples, strings)'''
f= ["apple", "banana", "cherry"]
for i in f:
    print(i)

# While loop
'''
executes a block of code as long as a specified condition is true.
'''
c = 0
while c < 6:
    print(c)
    c+= 1


# Jumping Statements

# break statement
#terminates the current loop and transfers control to the next statement outside the loop.
for i in range(10):
    if i == 5:
        break
    print(i)

# continue statement
#kips the current iteration of the loop and moves to the next iteration
for i in range(10):
    if i == 5:
        continue
    print(i)


# Special Functions
n= ["arpita", "sunita", "shivam"]

# len()
print(len(n))  # Output: 3

# id()
print(id(n))  # Output: Unique ID of the list object

# type()
print(type(n))  # Output: <class 'list'>

# range()
for i in range(5):
    print(i)  # Output: 0 1 2 3 4


