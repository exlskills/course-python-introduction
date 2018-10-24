### Even more complexity

Here is the question that we will be solving in this slide:

Given a list, write a function called _index_equals_ that **returns** only the values inside the list that where the index matches the value in the list.

**Remember: In python the index always starts at 0**

- Initially this is not going to return anything and may even give you an error

Examples:
```python
list_1 = [0,1,3,4,6]
index_equals(list_1) # should return [0,1]

list_2 = [1,1,2,3,6]
index_equals(list_1) # should return [1,2,3]
```
As well, I am going to introduce a python built in function that is called **enumerate** which is super useful in _for_ loops.

### Actual Definition:
Enumerate is a built-in function of Python. It’s usefulness can not be summarized in a single line. Yet most of the newcomers and even some advanced programmers are unaware of it. It allows us to loop over something and have an automatic counter. Here is an example:

```python
# Define the list
my_list = ['apple', 'banana', 'grapes', 'pear']

# Iterate through the list and add a counter using enumerate
for c, value in enumerate(my_list):

    # print the counter and the value
    print(c, value)

# Output:
# 0 apple
# 1 banana
# 2 grapes
# 3 pear
```

### Back to index_equals
Now you may be beginning to see where I am going with this.  Using the **Enumerate** function we can see if the value in our list is the same as the index!  

### Steps to a solution:
1.  Create a function that takes in a list and returns a list
2.  Interate through the list and check to see if the value equals the index
3.  If the value meets our conditions add it to a new list
4.  Return the new list

### Solution TEST
```python
def index_equals(lst):
  '''
  INPUT: lst = list of integers
  OUTPUT: new_list = list of integers from the original list if the value matches the index
  '''
  # Create the new list that we are going to return
  new_list = []

  # Iterate through the original list and enumerate the items in it
  for i,value in enumerate(lst):

    # Create our logic statement to check our condition
    if i == value:

      # If it meets the conditions, append it to the new list
      new_list.append(value)

  # Return the new list
  return new_list


# Test it out
list_1 = [0,1,3,4,6]
index_equals(list_1) # should return [0,1]

list_2 = [1,1,2,3,6]
index_equals(list_1) # should return [1,2,3]
```
