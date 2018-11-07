def print_list(list):
	print()
	print("List is ")
	for item in list:
		print(item)
	print("=========")
	print()

# Initialize List
print("Initialize List")
colors = ["red","green","blue","violet","indigo","black","white","silver"]
print_list(colors)

# Adding Elements
print("Adding Elements")
colors.append("yellow")
colors.insert(1,"orange")
print_list(colors)

# Deleting Elemets
print("Deleting Elemets")
del colors[1]
colors.remove("yellow")
print_list(colors)

# Popping Elemets
print("Popping Elements")
last_element = colors.pop()
first_element = colors.pop(0)
print("first_element --> " + first_element)
print("last_element --> "+last_element)
print_list(colors)

# Length of list
length = len(colors)
print("Length of list is " + str(length))
print()

# Sorting
print("Temporary Asc Sort")
print_list(sorted(colors))

print("Temporary Dsc Sort")
print_list(sorted(colors,reverse = True))

print("Permanent Asc Sort")
colors.sort()
print_list(colors)

print("Permanent Dsc Sort")
colors.sort(reverse = True)
print_list(colors)

# Creating lists using range function
numbers = list(range(1,11))
print_list(numbers)

# Min, Max, Sum of list
minumum = min(numbers)
maximum = max(numbers)
sum_list = sum(numbers)
print("minumum --> "+str(minumum))
print("maximum --> "+str(maximum))
print("sum_list --> "+str(sum_list))

# Slicing  list [ startIndex : endIndex+1 ]
sliced_colors = colors[2:4]
print_list(sliced_colors)
sliced_colors_start = colors[:4]
print_list(sliced_colors_start)
sliced_colors_end = colors[2:]
print_list(sliced_colors_end)

# Create a copy using slice
colors_copy = colors[:]
print_list(colors_copy)

# List Comprehensions

## Long Approach
squares = []
for x in range(1, 11):
    square = x**2
    squares.append(square)

print_list(squares)

## Short Approach

squares_new = [ x**2 for x in range(1,11) ]
print_list(squares_new)
