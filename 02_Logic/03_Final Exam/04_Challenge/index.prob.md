>> Write code that satisfies the following <<

Taking the list `lst = range(1000)` write code that sums all the values that are either divisible by 32 or divisible by 22.  

Your code should output **37586**

Solution:
```python
lst=range(1000)

s = 0

for val in lst:
    if (val % 22 == 0) or (val % 32 == 0):
    s += val
```

|| Check out the previous lectures! ||
