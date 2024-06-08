# EXCEPTION HANDLING
'''
-- an exception is an error that disrupts the normal flow of a program's execution. 
-- Error in Python can be of two types i.e. Syntax errors and Exceptions.
'''

# IndexError
numbers = [1, 2, 3]
try:
  print(numbers[5])  # This will raise an IndexError
except IndexError:
  print("Invalid index accessed")


# TypeError
try:
  print(10 + "hello")  # This will raise a TypeError (can't add int and str)
except TypeError:
  print("Unsupported operation between types")

# ValueError
try:
  age = int("hello")  # This will raise a ValueError (invalid string for int conversion)
except ValueError:
  print("Invalid value for integer conversion")

# ZeroDivisionError
try:
  result = 10 / 0
except ZeroDivisionError:
  print("Cannot divide by zero")


# Handling Exceptions at Different Levels:

# Local level
def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except ZeroDivisionError:
        return "Cannot calculate average of an empty list"

# Global level 
try:
  result = 10 / 0
except ZeroDivisionError:
  print("Oops! You can't divide by zero")

class PalindromeError(Exception):
    pass

def is_palindrome(input_str):
    if not isinstance(input_str, str):
        raise PalindromeError("Input must be a string")
    clean_str = input_str.replace(" ", "").lower()
    if clean_str == clean_str[::-1]:
        return True
    else:
        return False
try:
    print(is_palindrome("racecar")) 
    print(is_palindrome("A man a plan a canal Panama"))  
    print(is_palindrome(123))  
except PalindromeError as e:
    print(e)
     
