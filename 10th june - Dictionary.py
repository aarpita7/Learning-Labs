# Dictionary
'''
-- it is an unordered collection of key-value pairs. 
-- it is a mutable data type. 
-- are useful for storing and retrieving data in an efficient and flexible way.
'''
'''
clear()	            Removes all the elements from the dictionary
copy()	            Returns a copy of the dictionary
fromkeys()	        Returns a dictionary with the specified keys and value
get()	            Returns the value of the specified key
items()	            Returns a list containing a tuple for each key value pair
keys()	            Returns a list containing the dictionary's keys
pop()	            Removes the element with the specified key
popitem()	        Removes the last inserted key-value pair
setdefault()	    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	        Updates the dictionary with the specified key-value pairs
values()	        Returns a list of all the values in the dictionary
'''
# Methods
# Create a dictionary with Indian names and details
person_info = {
    "Name": "Arpita",
    "Age": 18,
    "City": "Ambala",
}

# Accessing values by key
name = person_info["Name"]
age = person_info["Age"]
print(f"Name: {name}, Age: {age}")

# Adding a key-value pair 
person_info["Profession"] = "Software Developer"
print("Person info after adding:", person_info)

# Checking for key existence
has_email_key = "Email" in person_info
print(f"Does 'Email' key exist? {has_email_key}")

# Updating a value
person_info["City"] = "Chennai"
print(f"Updated City: {person_info['City']}")

# Removing a key-value pair
removed_profession = person_info.pop("Profession")
print(f"Removed Profession: {removed_profession}")

fav_color = person_info.get("Favorite Color", "Blue")  
print(f"Favorite Color (if exists): {fav_color}")



person = {
    'name': 'Arpita Mahapatra',
    'age': 18,
    'address': {
        'street': '123 Main St',
        'city': 'Ambala cantt',
        'state': '  HY'
    }
}

print(person['name'])  
print(person['address']['city'])


# Counting word occurrences in a sentence
sentence = "Hello, world! Hello, Python!"
wcounts = {}

for i in sentence.split():
    if i in wcounts:
        wcounts[i] += 1
    else:
        wcounts[i] = 1

print(wcounts) 

my_dict = {'arpita': 1, 'sunita': 2, 'shivam': 3}
removed_value = my_dict.pop('shivam')
print(removed_value) 
print(my_dict) 

my_dict.clear()
print(my_dict)

person['email'] = 'arpita@example.com'
popped_value = person.pop('age')

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]

# Dictionary with squares of numbers
squares = {num: num**2 for num in numbers}
print(squares)

# Finding common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)
print(common_elements)  

# Counting unique elements
elements = [1, 2, 3, 1, 2, 4, 5, 5]
unique_counts = {element: elements.count(element) for element in set(elements)}
print(unique_counts) 


def invert_dict(dictionary):
    inverted = {value: key for key, value in dictionary.items()}
    return inverted

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)

# List of dictionaries
data = [
    {"name": "Arpita", "age": 18, "city": "Ambala"},
    {"name": "Sunita", "age": 42, "city": "Ambala"},
    {"name": "Shivam", "age": 15, "city": "Silligudi"},
    {"name": "Shanvi", "age": 45, "city": "Mumbai"}
]

filtered_data = [person for person in data if person["age"] > 30]

print(filtered_data)

