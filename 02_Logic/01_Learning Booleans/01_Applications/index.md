# Applications of If Statements

In the previous section we covered iterables which we can set up a for loop with.  Lets consider a situation where we want to take a list for each number in the list, if it is divisible by three then we want to add it to the sum.  Otherwise, we will want to move onto the next number.

Lets say that our list is: `lst = [3,10,33,14]`

In this case, our result would be 36 as 3 and 33 are the only numbers that are divisible by 3

#### Steps to a solution
1. Start a sum = 0
2. Go through every number in the list
3. If the number is divisible by 3, add it to the sum (check number modulus 3 == 0)
4. Otherwise keep going through the list
#### Solution
```Python
lst = [3,10,33,14]

#Initialize the sum
s = 0

#Iterate through all the numbers in the list
for number in lst:

  #if the number meets our condition, add it to the sum
  if number % 3 == 0:
    s += number

# Print out the sum after the loop
print(s)
```
