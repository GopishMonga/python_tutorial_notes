# Strings
## Strings are arrays of bytes representing Unicode characters.
## However, Python does not have a character data type,
## a single character is simply a string with a length of 1.

# Initialize String
## Strings can be initialized with single,double and triple quotes
string1 = 'Hello World!'
string2 = "Let's try 'single quotes'"
string3 = '''Let's try "double quotes" '''
string4 = '''This string is
                    a multiple line
            string. '''

print(string1)
print(string2)
print(string3)
print(string4)

# Accessing characters
## individual characters accessed by Indexing
## Negative index can be used to access from end of string
## While accessing an index out of the range will cause an IndexError
## Only Integers are allowed to be passed as an index, float or,
## other types will cause a TypeError

name = "Gopish Monga"
first_char = name[0]
last_char = name[-1]
print(name)
print(first_char)
print(last_char)

## Slicing can be used to access substrings
print(name[3:6])
print(name[3:-2])
