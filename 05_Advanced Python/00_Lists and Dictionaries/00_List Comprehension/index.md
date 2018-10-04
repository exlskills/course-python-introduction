### Advanced Python

We are getting very close to finishing our intro to python course, but there are a couple of interesting applications that you will come across that I will introduce here.  

## List Comprehension

Using a list, you can actually put a for loop inside.  This is a great way to get a list that meets certain specifications.  

```python
x = [i for i in range(10)]
```
This sets x equal to the list `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`

Lets say for example that you want only values between 1 and 100 that are divisible by 10.  In that case, we would use the following list comprehension:
```python
x = [i for i in range(100) if i % 10 == 0]
```
This sets x equal to the `[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]` which is exactly what we want!  

At first list comprehension can seem extremely complicated, but as you work on it, you will notice that it will become very intuitive.
