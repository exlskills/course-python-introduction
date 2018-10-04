

### Tuples

**Definition:** Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

To define a tuple, you use parentheses rather than square brackets.  These act very similarly to list in many ways including with iteration.

```python
tuple1 = (1,2,3)
tuple2 = tuple([1,2,3])
```
Just like with list, you access the data using indexes and you can iterate through the data.  The biggest difference between a tuple and a list is that list are **mutable** while tuples are **immutable**.

This means that in python given a list and a tuple:

```python
list1 = [1,2,3,4]
tuple1 = (1,2,3,4)
```

If we wanted to change the first value, it would only work in the list and not the tuple.

```python
list1[0] = 10 # This works!!
tuple1[0] = 10 # This doesn't work, will throw and error
```

Tuples can be put into lists, and vice versa, but I tend to find that Tuples are most useful for holding `x,y` pairs or `x,y,z` pairs in a list.

Below you can find a list of tuples that represent `x,y` coordinates!

```python
x_y_list = [(1,1),(2,3),(3,3),(2,1)] # This is a list of Tuples
```
