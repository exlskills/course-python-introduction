# Functions and Iterables

- Since we just introduced a list, one of the most useful parts of a list is that they are an **iterable**

An iterable is a collection of data that you can move through using a `for loop`

**For Loop** Syntax in python

```python
lst = [1,2,3,4]

# Print out each number in the List
for number in lst:
  print(number)
  ```

You can iterate through many different objects including *strings*

This would be a good time to go ahead and play around with the following code segments in an IDE.  Run each segment separately, and try to understand what is going on in each

```python
string = 'Hello'

# Print out each number in the List
for letter in string:
  print(letter)
```

```python
lst_string = ['Hello','World']

# Print out each number in the List
for thing in lst_string:
  print(thing)
```

### The range() Function

To loop through a set of code a specified number of times we can use the range() function.

The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
```python
for x in range(6):
  print(x)
```

- The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

```python
# Start at number 2 and go through 5
for x in range(2,6):
  print(x)
```
- The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: `range(2, 30, 3)`

```python
for x in range(2, 30, 3):
  print(x)
```
