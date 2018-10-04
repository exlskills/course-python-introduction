### Sets


Set in Python is a data structure equivalent to sets in mathematics. It may consist of various elements; the order of elements in a set is undefined. You can add and delete elements of a set, you can iterate the elements of the set, you can perform standard operations on sets (union, intersection, difference). Besides that, you can check if an element belongs to a set.

Unlike arrays, where the elements are stored as ordered list, the order of elements in a set is undefined (moreover, the set elements are usually not stored in order of appearance in the set; this allows checking if an element belongs to a set faster than just going through all the elements of the set).

Sets are very similar to dictionaries (we will get into **dictionaries** more later) and are defined using a special keyword.

```python
new_set = set([1,2,3])
```
But when they print out they use the curly braces. For example if we where to print out `new_set` it would print `{1,2,3}`
