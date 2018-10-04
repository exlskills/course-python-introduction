### Using Dictionaries in our code

To initialize a new dictionary you would use curly braces:

```python
dictionary = {}
```
Once you have created your dictionary, you can start adding key value pairs to it.  The key must be a `string`,`float`,`integer` or `tuple`.  The value can be any type of data structure you would like including a `list` or `set`

Below is a couple of examples of adding different types of keys and values to the dictionary.
1. Adding a integer key and string value
  - Lets imagine an example where we would like to map each letter to its placement in the alphabet.  In this example, I will show how to map the first few letters.

```python
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)
```
This prints out: `{'a': 1, 'b': 2, 'c': 3, 'd': 4}`

- One thing to take into account is that it may look ordered but really, it has no absolute order.  

2. Keys

To access all the keys in a dictionary, you will use the method `.keys()`
```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.keys())
```
This prints out `dict_keys(['a', 'b', 'c', 'd'])` which can be iterated through in a for loop.  
3. Values

To access all the values that the key pairs point to, you will use the method `.values`
```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.items())
```
This returns `dict_values([1, 2, 3, 4])` which can be iterated through.


4. Items

To access all the items in a dictionary, you will use the method `.items()`

```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d.items())
```
This returns a list of tuples that contain each item in the dictionary.  Once again you can iterate through this list of tuples.  


5. Looking up values by a Key

This is where a dictionary comes in super useful. You can look up the value associated with any of the keys.

```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d['a'])
````
This would print the value 1 since the key `a` has a value of 1 associated with it.  This can be done with any key in a dictionary, but will return an error if you try to use a key that does not exist in a dictionary.  

You can check to see if a dictionary contains a specific key by using the `in` operator.


```python
d= {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'a' in d #True
'f' in d #False
````
