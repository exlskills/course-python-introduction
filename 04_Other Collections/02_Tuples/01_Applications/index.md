### Using Tuples in your code!

1. Length of a Tuple
```python
tup = (1,2,3)

print(len(tup)) # will return 3!
```
2. Concatenation of Tuples
```python
tup1 = (1,2,3)
tup2 = (3,4,5)


print(tup1 + tup2)  # Will return (1,2,3,4,5,6)
```
3. Repetition
```python
tup = ('hello',)*4

print(tup)

# Returns ('hello', 'hello', 'hello', 'hello')
```
4. Membership
```python
print(3 in (1, 2, 3))  #returns True
```
5. Iteration:
```python
for x in (1, 2, 3):
  print(x)

# prints out 1,2,3
```

Built in functions:
- `len(tuple)` gives the length
- `max(tuple)` gives the max value
- `min(tuple)` gives the min value
- `tuple(seq)` turns a sequence into a tuple
