# Set is an unordered collection of data type that is iterable,
# mutable and has no duplicate elements

# Initialization
set1 = set()
print('\nInitialized empty set')
print(set1)

# Initialization with String
set1 = set("Helloo Worrrlddd!!!!")
print('\nSet initialized with string')
print(set1)

# Initialization with list
set1 = set([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5])
print('\nSet initialized with list')
print(set1)

# Initialization with mixed data types
set1 = set(["hello",1,1,2,3,"world"])
print('\nSet initialized with list')
print(set1)

# Adding element to the Set
set1.add(8)
set1.add(9)
set1.add(12)
print("\nSet after Addition of Three elements: ")
print(set1)

# Adding elements to the Set using Iterator
for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

# Adding Tuples to the Set
set1.add((6,7))
print("\nSet after Addition of a Tuple: ")
print(set1)

# Addition of elements to the Set using Update function
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)

# Creating a Set
set1 = set([1, 2, 3, 4, 5, 6,
            7, 8, 9, 10, 11, 12])
print("Intial Set: ")
print(set1)

# Removing elements from Set using Remove() method
# If element doesn't exist in set, then error is thrown
set1.remove(5)
set1.remove(6)
print("\nSet after Removal of two elements: ")
print(set1)

# Removing elements from Set using Discard() method
set1.discard(8)
set1.discard(9)
print("\nSet after Discarding two elements: ")
print(set1)

# Removing elements from Set using iterator method
for i in range(1, 5):
    set1.remove(i)
print("\nSet after Removing a range of elements: ")
print(set1)

# Removing element from the Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)

# Removing all the elements from Set using clear() method
set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)
