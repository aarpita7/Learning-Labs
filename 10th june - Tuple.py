# Tuple
'''
They are indexed.
Tuples are ordered.
These are immutable.
They can contain duplicate items.
'''

fruits = ("apple", "banana", "cherry")
print("Fruits:", fruits)

first_fruit = fruits[0]
last_fruit = fruits[2]
print(f"First fruit: {first_fruit}")
print(f"Last fruit: {last_fruit}")

#

new_fruits = fruits[:1] + ("kiwi",) + fruits[2:]
print("New fruits:", new_fruits)

data_tuple = ("name", 25, 3.14, True)
print("Mixed data tuple:", data_tuple)

name = data_tuple[0]
age = data_tuple[1]
print(f"Name: {name}")
print(f"Age: {age}")

numbers = (1, 2, 2, 3, 1)
print("Numbers with duplicates:", numbers)

dupe_count = numbers.count(2)
print(f"Number of 2s: {dupe_count}")

coords = (10, 20)  
x = coords[0]
y = coords[1]
print(f"Coordinates: ({x}, {y})")

record = ("Arpita", 18, "Engineer")
name = record[0]
profession = record[2] 
print(f"Record: {name}, {profession}")

# Slicing 
# Sample tuple
my_tuple = ("apple", "banana", "cherry", "orange", "mango")

# Positive Slicing
fruits = my_tuple[1:3] 
print("Sliced fruits:", fruits)

rest_of_tuple = my_tuple[1:]  
print("Rest of the tuple:", rest_of_tuple)

first_part = my_tuple[:4]  
print("First part of the tuple:", first_part)

# Negative Slicing
last_fruits = my_tuple[-2:] 
print("Last two elements:", last_fruits)

reversed_slice = my_tuple[-2:1]  
print("Reversed slice:", reversed_slice)

copied_tuple = my_tuple[:]  
print("Original tuple:", my_tuple)
print("Copied tuple:", copied_tuple)


# returns the smallest element in the sequence.
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = ("mango", "kiwi", "grape")

sflist = min(fruits_list)
sftuple = min(fruits_tuple)

print("Smallest fruit in list:", sflist)  # Output: apple
print("Smallest fruit in tuple:", sftuple)  # Output: grape

# returns the largest element in the sequence.
numbers_list = [1, 5, 2, 8]
numbers_tuple = (3, 7, 9, 0)

largest_number_list = max(numbers_list)
largest_number_tuple = max(numbers_tuple)

print("Largest number in list:", largest_number_list)  # Output: 8
print("Largest number in tuple:", largest_number_tuple)  # Output: 9
     

# sorts the elements of the list in-place
mixed_list = ["apple", 3, 9.5, True]

mixed_list.sort()  # Sorts the list in-place

print("Sorted list:", mixed_list)


# calculates the sum of all the elements in the sequence (assumes numeric data)
numbers_list = [4, 7, 2, 11]
numbers_tuple = (6, 3, 8, 1)

list_sum = sum(numbers_list)
tuple_sum = sum(numbers_tuple)

print("Sum of list elements:", list_sum)  # Output: 24
print("Sum of tuple elements:", tuple_sum)  # Output: 18

numbers_list = [1, 5, 2, 8, 3]
largest = max(numbers_list)
print("Largest number:", largest) 
numbers_tuple = (10, 20, 30)
largest = max(numbers_tuple)
print("Largest number in tuple:", largest)