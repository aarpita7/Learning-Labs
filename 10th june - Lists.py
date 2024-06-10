# Lists
'''
Append: adds a single.
Insert: insert a new element at a specified position.
Remove: remove the first occurrence of a specified element.
Copy (shallow and deep copy): allow you to create copies of lists.
-- shallow copy creates a new list object but still refers to the original elements. 
-- deep copy creates a new list as well as new copies of the elements within it.
Count: returns the number of occurrences of a specified element.
Extend: append elements from another iterable to the end of the current list.
Index: returns the index of the first occurrence of a specified element within the list.
Sort: sort the elements of the list in ascending order (by default) or in a specified order.
Reverse: reverses the order of the elements in the list.
Clear: remove all elements from the list, leaving it empty.
Pop: removes and returns the element at the specified position in the list. 
-- If no index is specified, it removes and returns the last element.
'''

# Initialize an empty list
my_list = []

# Append elements 
elements = input("Enter elements separated by spaces to add: ").split()
my_list.extend(elements)
print(f"Elements added: {my_list}")

# Insert an element
element = input("Enter element to insert: ")
position = int(input("Enter position (0-based indexing, or -1 for the end): "))
my_list.insert(position if 0 <= position <= len(my_list) else len(my_list), element)
print(f"{element} inserted at position {position}.")

# Remove the first occurrence (using `in` for existence check)
element = input("Enter element to remove: ")
if element in my_list:
    my_list.remove(element)
    print(f"{element} removed from the list.")
else:
    print(f"{element} not found in the list.")

# Shallow copy
copy_list = my_list.copy()
print("Shallow copy created:", copy_list)

# Deep copy reminder 
print("Deep copy requires additional libraries for complex data types.")

# Count occurrences
element = input("Enter element to count: ")
count = my_list.count(element)
print(f"{element} appears {count} times in the list.")

# Extend with another list 
new_list_name = input("Enter another list name (or leave blank to continue): ")
if new_list_name:
  try:
    new_list = eval(new_list_name)  # Assuming the variable holds a list
    my_list.extend(new_list)
    print(f"Elements extended from {new_list_name}: {my_list}")
  except (NameError, SyntaxError):
    print("Invalid list name or format.")

# Sort or Reverse 
sort_choice = input("Sort (ascending) or Reverse the list (y/n)?: ").lower()
my_list.sort() if sort_choice in ('y', 'yes') else my_list.reverse()
print(f"List {(sort_choice if sort_choice in ('y', 'yes') else 'reversed')}: {my_list}")

# Pop 
print(f"Last element removed: {my_list.pop()}")

print("Final list:", my_list)

# List Comprehension
# new_list = [expression for item in iterable if condition]
even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)

# Indexing

fruits = ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0]) 
print("Last fruit:", fruits[-1]) 

# Updating elements
fruits[1] = "kiwi"  
print("Updated list:", fruits)


# Slicing

fruits = ["apple", "banana", "cherry", "orange", "mango"]

# Positive slicing
print("Fruits from 1 to 3 (excluding 3):", fruits[1:3])  

# Negative slicing
print("Last two fruits:", fruits[-2:]) 

# Update elements within a slice
fruits[2:4] = ["kiwi"]  
print("List after update:", fruits)

# Insert elements
fruits[1:1] = ["pineapple"] 
print("List after inserting:", fruits)

# Reduce 
def reduce(func, ite, ini=None):
  accum = ini
  for i in ite:
    if accum is None:
      accum = i
    else:
      accum = func(accum, i)
  return accum

words = ["apple", "banana", "cherry"]
def add_lengths(total, word):
  return total + len(word)
total_length = reduce(add_lengths, words)
print("Total length of words:", total_length)


# Map 
numbers = [1, 2, 3]
def double(x):
  return x * 2
doubled_numbers = list(map(double, numbers))
print("Doubled numbers:", doubled_numbers)


# Filter
numbers = [1, 2, 3, 4]
def is_even(x):
  return x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)


# Zip
names = ["Arpita", "Sunita", "Shivam"]
ages = [18, 42, 15]
name_age_pairs = list(zip(names, ages))
print("Name-age pairs:", name_age_pairs)






