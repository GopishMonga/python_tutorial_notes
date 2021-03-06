# Dictionary in Python is an unordered collection of data values,
# used to store data values like a map, which unlike other Data Types
# that hold only single value as an element, Dictionary holds key:value pair.
# Key value is provided in the dictionary to make it more optimized.
# Each key-value pair in a Dictionary is separated by a colon :,
# whereas each key is separated by a comma.
# Keys of a Dictionary must be unique and of immutable data type such as
# Strings, Integers and tuples, but the key-values can be repeated and be of any type.

def print_dictionary(dictionary):
	print("\nDictionary Contents")
	print("--------------------------------------------")
	for key,value in dictionary.items():
		print("--> " + str(key) + " : " + str(value))
	print("\n")

# Initialize Dictionary
man = {"firstName":"Gopish","lastName":"Monga","age":24}
print_dictionary(man)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# Creating a Nested Dictionary
Dict = {1: {'A' : 'Geeks', 'B' : 'For', 'C' : 'Geeks'},
        2: {'D' : 'Welcome', 'E' : 'To', 'F' : 'Geeks'}}
print("\nNested Dictionary: ")
print(Dict)

# Accessing Values

## Using [key]  ===> only use when key exists, otherwise error is thrown
firstName = man["firstName"]
print("\nfirstName = " + firstName)

## Using get method ===> returns None if key not found, also default value can be given
height = man.get("height","5 feet 8 inches")
print("\nheight = " + height)

# Adding elements
print("\nAdding height")
man["height"] = "5 feet 8 inches"
print_dictionary(man)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

# Initial Dictionary
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a Key using pop()
Dict.pop(5)
print("\nPopping specific element: ")
print(Dict)

# Deleting a Key using popitem()
Dict.popitem()
print("\nPops first element: ")
print(Dict)

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)

# Accessing keys
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
        'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
        'B' : {1 : 'Geeks', 2 : 'Life'}}
print_dictionary(Dict)
print("\nKeys in this dictionary are")
for key in Dict.keys():
	print(key)

# Accessing values
print("\nValues in this dictionary are")
for value in Dict.values():
	print(value)

# Accessing pair of key & value
print("\nItems in this dictionary are")
for item in Dict.items():
	print(item)
