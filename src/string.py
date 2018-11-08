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

## Strings are immutable, so they can't be updated
## So, we need to create new string and assign to same variable
name = name + "!!!"
print(name)

## Deleting Strings
del name
### print(name) will through an error "name is not defined"

# Escape Sequence
## Initial String
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ")
print(String1)

## Escaping Single Quote
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

## Escaping Doule Quotes
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

## Printing Paths with the use of Escape Sequences
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ")
print(String1)

## Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

## Using raw String to ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)
