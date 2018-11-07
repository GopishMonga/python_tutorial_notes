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