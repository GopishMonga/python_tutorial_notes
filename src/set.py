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

# Frozen sets in Python are immutable objects that only support methods and
# operators that produce a result without affecting the frozen set or
# sets to which they are applied.

# Initialization of empty frozen set
print("\nInitialized frozen set")
print(frozenset())

# Initialization of non-empty frozen set
frozen_set1 = frozenset("GEEKSFORGEEKS")
print(frozen_set1)

# Set Operations can be also be performed in python
set1 = set([1,2,3,4])
set2 = set([3,4,5,6])
print(set1)
print(set2)
# Union Operation
print("\nUnion of Sets")
set3 = set1.union(set2)
print(set3)
# Intersection
print("\nIntersection of Sets")
set4 = set1.intersection(set2)
print(set4)
# Difference
print("\nDifference of Sets")
set5 = set1.difference(set2)
print(set5)
# Disjoint function
print("set1 and set2 are disjoint?", set1.isdisjoint(set2))
print("set4 and set5 are disjoint?", set4.isdisjoint(set5))
# Subset function
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(C))
print(C.issubset(B))
# Superset function
print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))
print("A.issuperset(C) : ", A.issuperset(C))
print("C.issuperset(B) : ", C.issuperset(B))
