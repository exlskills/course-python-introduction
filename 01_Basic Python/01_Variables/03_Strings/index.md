### Another type of variable: Strings
A string in python is a variable that contains text.  This can take many forms, and a string can contain numbers in the form of text.  Here are a couple of examples of strings.


```python
# Declare a string:

# Strings can be multiple letters
string1 = 'Hello World'

# Strings can hold a text representation of a number
string2 = "1"

# Strings can hold a text representation of multiple numbers
string3 = '1 2 3'

# Print each out
print(string1)
print(string2)
print(string3)
```

#### Official Definition:
String literals in python are surrounded by either single quotation marks, or double quotation marks.

``'hello'`` is the same as ``"hello"``.

Strings can be output to screen using the print function


As well, there are a couple of methods that exist that can be used with strings. I will introduce a few.

- You can find the length of a string using `len()`
- Turn a string into all lower case `string.lower()`
- The same works with `.upper()` method
- Split a string using the `.split()` method

```python
# Declare the string
string1 = 'Hello World'

# This will pint the length of the string
print('The length of the string is: ', len(string1))

#This will print the string  `hello world`
print('The string in all lower case letters is: ', string1.lower())

#This will print the string  `HELLO WORLD`
print('The string in all UPPER case letters is: ', string1.upper())

#This will print the two strings 'Hello', 'World'
print('The string split into a bunch of words is: ',string1.split(' '))
```
