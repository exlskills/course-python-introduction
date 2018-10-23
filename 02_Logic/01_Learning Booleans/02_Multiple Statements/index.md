### More than one conditional statement


You can put multiple conditions together in that statement.  

Lets consider a situation where we want to go through all the numbers in a list and sum all the values that are between 4 and 7.  For example is our list is: `lst = [1,5,4,12,18,6]` our result would be 5+4+6 = 15

Steps to a solution:

1. Create sum = 0
2. Iterate through list of numbers
3. If the number > 3 **and** number < 7, add it to the sum

Solution:
```python
lst = [3,10,33,14]

#Initialize the sum
s = 0

#Iterate through all the numbers in the list
for number in lst:

  #if the number meets our condition, add it to the sum
  if (number > 3) and (number < 7):
    s += number

# Print out the sum after the loop
print(s)
```


### Or Statements
As well, instead of using and, we can use the or statement.  Lets say you have a list of words, and you only want to print out the word if it is more than 5 characters long **or** it contains the letter s.

For example, if our list was: `lst = ['hello', 'world', 'I', 'really','like','cats']`

we would want to print out:
```
really
cats
```
To do this we would implement the following code:
```python
lst = ['hello', 'world', 'I', 'really','like','cats']

# Iterate through all the words
for word in lst:

  # Add our condition (more than 3 letters or contains 's')
  if (len(word) > 5) or ('s' in word ):

    # If it met our condition, print the wordexit
    print(word)
```
