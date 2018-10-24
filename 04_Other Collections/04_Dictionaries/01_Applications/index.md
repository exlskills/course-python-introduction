### Using Dictionaries in our code

To initialize a new dictionary you would use curly braces:

```
dictionary = {}
```
Once you have created your dictionary, you can start adding key value pairs to it.  The key must be a `string`,`float`,`integer` or `tuple`.  The value can be any type of data structure you would like including a `list` or `set`

Below is a couple of examples of adding different types of keys and values to the dictionary.
1. Adding a integer key and string value
  - Lets imagine an example where we would like to map each letter to its placement in the alphabet.  In this example, I will show how to map the first few letters.

```python
# create the dictionary
d = {}

# add to it
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

#print it out
print(d)
```
This prints out: `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`

- One thing to take into account is that it may look ordered but really, it has no absolute order.  

2. Keys

To access all the keys in a dictionary, you will use the method `.keys()`
```python
# Declare the dictionary
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print out the keys
print(d.keys())
```
This prints out `dict_keys(['a', 'b', 'c', 'd'])` which can be iterated through in a for loop.  
3. Values

To access all the values that the key pairs point to, you will use the method `.values`
```python
# Declare the dictionary
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print out the values
print(d.values())
```
This returns `dict_values([1, 2, 3, 4])` which can be iterated through.


4. Items

To access all the items in a dictionary, you will use the method `.items()`

```python
# Declare the dictionary
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# print the items
print(d.items())
```
This returns a list of tuples that contain each item in the dictionary.  Once again you can iterate through this list of tuples.  


5. Looking up values by a Key

This is where a dictionary comes in super useful. You can look up the value associated with any of the keys.


```python
# Declare the dictionary
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Print out the value that corresponds to a
print(d['a'])
````
This would print the value 1 since the key `a` has a value of 1 associated with it.  This can be done with any key in a dictionary, but will return an error if you try to use a key that does not exist in a dictionary.  

You can check to see if a dictionary contains a specific key by using the `in` operator.


```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'a' in d #True
'f' in d #False
````
