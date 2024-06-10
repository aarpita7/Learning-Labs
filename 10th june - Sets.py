# Sets 
'''
-- a set is an unordered collection of unique elements.
-- This means that a set cannot contain duplicate values
-- and the order of elements in a set is undefined
-- sets are a fundamental data structure in Python.
-- performing mathematical operations like union, intersection, and difference.
'''
mset = {1, 2, 3, 4, 5}
aset = set([4, 5, 6, 7, 8])
print(mset)
print(aset)

# Operations
# Union (|):
'''
-- combines all unique elements from two sets into a new set
-- excluding duplicates.
'''
s1 = {1, 2, 3}
s2 = {3, 4, 5}
uset = s1 | s2  # Output: {1, 2, 3, 4, 5}
print("Union:",uset)

# Intersection (&):
'''
-- finds elements that are common to both sets and returns them in a new set.
-- it only includes elements that exist in both sets.
'''
s1 = {1, 2, 3}
s2 = {3, 4, 5}
iset = s1 & s2  # Output: {3}
print("Intersection:",iset)

# Difference (-):
'''
-- subtracts elements of one set from another and returns the remaining elements in a new set. 
-- it includes elements that are present in the first set but not in the second set.
'''
s1 = {1, 2, 3}
s2 = {3, 4, 5}
dset = s1 - s2  # Output: {1, 2}
print("Difference:",dset)

# Symmetric Difference (^):
'''
-- generates a new set containing elements that are exclusive to each set. 
-- it includes elements that are present in either set, but not in both sets.
'''
s1 = {1, 2, 3}
s2 = {3, 4, 5}
sdset = s1 ^ s2  # Output: {1, 2, 4, 5}
print("Symmetric Difference:",sdset)


# Methods

# add(element):
my_set = {1, 2, 3}
print("Before add():",my_set)
my_set.add(4)
print("After add():",my_set)  # Output: {1, 2, 3, 4}

# remove(element):
my_set = {1, 2, 3}
print("Before remove():",my_set)
my_set.remove(2)
print("After remove():",my_set)  # Output: {1, 3}

# discard(element):
print("Before discard():",my_set)
my_set.discard(2)
print("After discard():",my_set)  # Output: {1, 3}

# pop():
my_set = {1, 2, 3}
print("Before pop():",my_set)
removed_element = my_set.pop()
print("After pop():",removed_element)  # Output: 1

# clear(): 
my_set = {1, 2, 3}
print("Before clear():",my_set)
my_set.clear()
print("After clear():",my_set)  # Output: set()

# copy():
my_set-{1,2,3}
print("Before copy():",my_set)
copied_set = my_set.copy()
print("After copy():",copied_set)  # Output: {1, 2, 3}

# update:
my_set = {1, 2, 3}
print("Before update():",my_set)
my_set.update([4, 5])
print("After update():",my_set)  # Output: {1, 2, 3, 4, 5}

#  issubset:
set1 = {1, 2}
set2 = {1, 2, 3, 4}
result = set1.issubset(set2)
print(result)  # Output: True

# issuperset:
set1 = {1, 2, 3, 4}
set2 = {1, 2}
result = set1.issuperset(set2)
print(result)  # Output: True

# isdisjoint:
set2 = {4, 5, 6}
result = set1.isdisjoint(set2)
print(result)  # Output: True

# Set Comprehension
even_squares = {x * x for x in range(1, 6) if x % 2 == 0}
print(even_squares)  # Output: {4, 16}

# Cartesian Product
set2 = {'a', 'b', 'c'}
cartesian_product = {(x, y) for x in set1 for y in set2}
print(cartesian_product)

