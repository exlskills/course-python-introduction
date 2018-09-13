## For loops with logic
We have already discussed iterables and logic statements, and even had one example with both in it. Now are are going to take a closer look at this and see how we can put this together in a stronger fashion.

Recall:
1. We can put multiple pieces of data into an **Iterable** called a _list_ and then create a `for loop` that will iterate through each value in the _list_
2. We can create `if` statements based the data that we are iterating through.

With this is mind, we can use these two functions together and create more complicated expressions. One example of this is that you have already seen is:

 _Lets consider a situation where we want to take a list for each number in the list, if it is divisible by three then we want to add it to the sum.  Otherwise, we will want to move onto the next number._

```Python
lst = [3,10,33,14]

#Initialize the sum
s = 0

#Iterate through all the numbers in the list
for number in lst:

  #if the number meets our condition, add it to the sum
  if (number % 3) == 0:
    s += number

# Print out the sum after the loop
print(s)
```

As we move on to more complex topics, you'll want to remember that it is all based on the basics you are learning right now.
