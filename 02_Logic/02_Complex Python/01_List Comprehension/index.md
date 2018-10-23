### Easy way to clean up your code

Lets talk a little bit about basic for loops for a while.  Imagine that you want to fill a list with the values from 0 - 10.  
- One way to do this is to create an empty list, iterate through the values between 0 and 5, and add the value to the list each time.  

Lets take a look at what this looks like:

```python
# Make an empty list
lst = []

# Go through the numbers between 0 and 11
for i in range(6):
  lst.append(i)
```

This will result in array that is equal to `[0,1,2,3,4,5]` **But there is a easier way to do this!**

Instead of having the for loop after initializing the list, we can have the for loop inside the list. This is called **List Comprehension** The following code will return the same list as the code above.


```python

x = [i for i in range(6)]

print(x)
```


See how much cleaner and shorter that is? T

We can also apply an if statement inside the list comprehension like we where talking about before.  

----
Example:  Lets consider a situation where we want to make a list where it only contains numbers that are divisible between 0 and 300 that are divisible by 27.

We can achieve this with
```python
x = [i for i in range(300) if i % 27 == 0]

print(x)
```
Which gives us back the list:`[0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270, 297]`

<div data-datacamp-exercise data-lang="r" data-height="500">
  <code data-type="pre-exercise-code"># no pec</code>
  <code data-type="sample-code">
    # Calculate 3 + 4
    3 + 4

    # Calculate 6 + 12
  </code>
  <code data-type="solution">
    # Calculate 3 + 4
    3 + 4

    # Calculate 6 + 12
    6 + 12</code>
  <code data-type="sct">
    test_output_contains(&quot;18&quot;, incorrect_msg = &quot;Make sure to add `6 + 12`
    on
    a new line. Do not start the line with a `#`, otherwise your R code is not executed!&quot;)
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
