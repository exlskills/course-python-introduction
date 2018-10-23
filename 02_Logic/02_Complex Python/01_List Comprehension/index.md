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

[i for i in range(6)]

```

See how much cleaner and shorter that is? T

We can also apply an if statement inside the list comprehension like we where talking about before.  

----
Example:  Lets consider a situation where we want to make a list where it only contains numbers that are divisible between 0 and 300 that are divisible by 27.

We can achieve this with
```python
[i for i in range(300) if i % 27 == 0]
```
Which gives us back the list:`[0, 27, 54, 81, 108, 135, 162, 189, 216, 243, 270, 297]`
