### Another type of variable: Strings
A string in python is a variable that contains text.  This can take many forms, and a string can contain numbers in the form of text.  Here are a couple of examples of strings.

```python
# These are strings
string1 = 'Hello World'
string2 = "1"
string3 = '1 2 3'

# Not a string
s = Hello World
s = 1
```

#### Official Definition:
String literals in python are surrounded by either single quotation marks, or double quotation marks.

``'hello'`` is the same as ``"hello"``.

Strings can be output to screen using the print function

```python
# This will print the string
string1 = 'Hello World'
print(string1)
```

As well, there are a couple of methods that exist that can be used with strings. I will introduce a few.

- You can find the length of a string using `len()`
- Turn a string into all lower case `string.lower()`
- The same works with `.upper()` method
- Split a string using the `.split()` method

```python
string1 = 'Hello World'

# This will pint the length of the string
print(len(string1))

#This will print the string  `hello world`
print(string1.lower())

#This will print the string  `Hello World`
print(string1.lower())

#This will print the two strings 'Hello', 'World'
print(string1.split(' '))
```
