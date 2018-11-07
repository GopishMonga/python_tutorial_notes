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
