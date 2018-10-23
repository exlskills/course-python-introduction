### Numbers with Decimals
In python a float refers to a number that has decimal places.  

Below, I create a variable x that is a float and then print value for x.  After this, I print out the `type` of the variable which is a _float!_

```python
# Define the variable
x = 3.2

# Print out the value
print('The value of x is:',x)

# Print out the type of variable x is
print(type(x))
```

#### Official Definition:

**float (floating point real values)** − Also called floats, they represent real numbers and are written with a decimal point dividing the integer and fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 102 = 250).


If you add a float and an int together, it results in a float!  An example of this is below, and you can see the result is `type` float
```python

# Declare x and y - One as an integer and one as a float
x = 3.2
y = 3

# Create the sum
z = x+y

# Print out the value and the type
print(z)
print(type(z))
```

This will give you a new variable `z` which is equal to 6.2

Calling the function `float(number)` will turn an integer into a number that can contain decimal places.
