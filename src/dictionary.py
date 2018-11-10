# Dictionary in Python is an unordered collection of data values,
# used to store data values like a map, which unlike other Data Types
# that hold only single value as an element, Dictionary holds key:value pair.
# Key value is provided in the dictionary to make it more optimized.
# Each key-value pair in a Dictionary is separated by a colon :,
# whereas each key is separated by a ‘comma’.

# Keys of a Dictionary must be unique and of immutable data type such as
# Strings, Integers and tuples, but the key-values can be repeated and be of any type.

def print_dictionary(dictionary):
	print()
	print("Dictionary Contents")
	print("--------------------------------------------")
	for key,value in dictionary.items():
		print("--> " + str(key) + " : " + str(value))
	print()
	print()

# Initialize Dictionary
man = {"firstName":"Gopish","lastName":"Monga","age":24}
print_dictionary(man)

# Accessing Values

## Using [key]  ===> only use when key exists, otherwise error is thrown
firstName = man["firstName"]
print("firstName = " + firstName)
print()

## Using get method ===> returns None if key not found, also default value can be given
height = man.get("height","5 feet 8 inches")
print("height = " + height)
print()

# Adding elements
print("Adding height")
man["height"] = "5 feet 8 inches"
print_dictionary(man)
