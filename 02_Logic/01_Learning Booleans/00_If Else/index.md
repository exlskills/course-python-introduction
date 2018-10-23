### Python Logic Statements

Just like in life, you can use a computer to make basic `if` statements.  This implies that `if` something meets a certain condition (based on what we learned with `Operators`) you can get the code to execute different code.  


The code below will print out the value 3 since it meets the condition
```python
# Define the variable
x = 3

# Set up the condition
if x == 3:
  print('x = 3')
```

There are a few different deviations from this that are also very useful.  They include the `elif` statement and the `else` statement.

- `elif` => if the first if statement is not executed, this will execute if the condition is met

- `else` => if none of the if statements are executed, this code will be executed

Below is situation where the elif will execute:

```python
# Declare the variable
x = 3

# Set up the condition
if x < 3:
  print('x < 3')

# Set up the elif condition
elif x == 3:
  print('x = 3')
```

And finally a situation where the else will execute:

```python

# Declare the variable
x = 3

# Set up the condition
if x < 3:
  print('x < 3')

# Set up the elif condition
elif x > 3:
  print('x > 3')

# Set up the else condition
else:
  print('x is not less than three and it is not greater than 3')
```
