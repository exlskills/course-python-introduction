### Adding more complexity

Within a function, we can do much more complicated processes and use this to minimize the number of lines of code that we are using.  For example, if we want to count the number characters in a string, we could use the following code:

```python
# The string we are trying to count letters in
string = 'Hello, you are learning python!'


#Create a count = 0 that we will update
count = 0

#Go through each letter in the string and increment the count
for letter in string:
  count += 1

print(count)
```
Obviously we could have done this with a call of `length(string)` as well, but this is to showcase how much a function can reduce the code length.


So if we made this into a function that returns the length of the string, it only requires 1 line to _call_ the function.

```python
def count_letters(string):
  #Create a count = 0 that we will update
  count = 0

  # Iterate through each letter in the string
  for letter in string:

    # update the counts each time
    count += 1
  return count
```

and then to use the functions we would just need to define our string and call the function on it:
```python

def count_letters(string):
  #Create a count = 0 that we will update
  count = 0

  # Iterate through each letter in the string
  for letter in string:

    # update the counts each time
    count += 1
  return count


  
string = 'Hello, you are learning python!'
print(count_letters)
```

This may seem arbitrary right now, but as we get into more difficult programming, this will become very useful!  In the next lecture we explore an example of a more difficult function that we will build together.
