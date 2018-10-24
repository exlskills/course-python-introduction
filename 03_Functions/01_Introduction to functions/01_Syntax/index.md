### Your First Function!

Below is the code for a function that adds all the numbers in a list and then sends back the sum.  We will explore each piece of the code directly

```python
def sum_numbers(lst):
  """
  This is a docstring, and it describes your function
  INPUT: lst is a list that we want to sum across
  OUTPUT: s is a scalar that is the sum of the list
  """
  # Declare the sum
  s = 0

  # Iterate through each number in the list
  for number in lst:

    # And add the number to the sum each time
    s += number

  # Return the sum
  return s

# Declare a new list
new_list = [1,2,3,4,3,2,1]

#Pass the list to the function we just created
print('The sum of the numbers in the list! ',sum_numbers(new_list))
```

Ok so the first line `def sum_numbers(lst):` is the declaration of our function.  
- def refers to _define_ and _sum_numbers_ is the name of our function.  

Functions then have parentheses which contain the arguments that are being passed to the function.  In this case, we are just passing a list and therefore lst is inside the parentheses.  

You may have a situation when you require no arguments and on the converse a situation where you require many arguments.

The next couple of lines should look familiar:
```python
lst = [1,2,3,4,5]
s = 0
for number in lst:
  s += number

print(s)
```
This is just a for loop that iterates through the list.

Finally, at the end we have the statement `return s`.  This is our return statement that sends back a value (or in some cases an object or list) back to where we called the function.  

Once you have built the function, you can easily call it using many different lists.  

To call the function, you must first define it, and then you can access it by running `sum_numbers(list)` in your python script

Also, don't forget to add your docstring so that someone else who wants to use your function can figure out what is going on!

### Challenge:
- What does **sum_numbers** return for the list `[1,1,1,1,15,2,1,2,3]`?
- How about `lst = range(100)`?


<div data-datacamp-exercise data-lang="python" data-height="500">
  <code data-type="pre-exercise-code"># no pec</code>
  <code data-type="sample-code">
  # Declare the list
  lst = range(100)

  # YOUR TURN:
  # calculate the sum of the numbers in the list!
  # Don't for get to print the results
  </code>
  
  <code data-type="solution">
  # Declare the list
  lst = range(100)

  # YOUR TURN:
  # calculate the sum of the numbers in the list!
  # Don't for get to print the results
  sum(range(100))</code>
  <code data-type="sct">
    test_output_contains(&quot;4950&quot;, incorrect_msg = &quot;Make sure to add 6 + 12
    on
    a new line. Do not start the line with a #, otherwise your R code is not executed!&quot;)
    success_msg(&quot;Awesome! See how the console shows the result of the R code you
    submitted? Now that you&#39;re familiar with the interface, let&#39;s get down to R
    business!&quot;)
  </code>
  <div data-type="hint">
    <p>Just add a line of R code that calculates the sum of 6 and 12, just like the
      example
      in the sample code!</p>
  </div>
</div>
