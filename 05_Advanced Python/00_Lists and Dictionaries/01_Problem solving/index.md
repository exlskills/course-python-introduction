### Applying your skills to Advanced Functions & Problem Solving

There will be multiple times when you encounter a hard problem that you need to solve.  In this basic course, I am going to outline the skill - solving process that I follow to get through these more difficult problems.  

Here we are going to solve the following problem:

_Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321) Make sure that if it is a negative number you keep the negative in the front (-123 becomes -321)_

I am going to write a function that solves this, and apply many of the skills that we have learned through this course.

1. Start with a function:
```python

def reverse_number(number):
  """
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  """
  pass
  #Reverse the number
  return reversed_number
```

2. When the number comes in, we want to turn it into a string, and then that string into a list.
```python

def reverse_number(number):
  """
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  """
  string_number = str(number)
  list_string_number = list(string_number)

  #Reverse the number
  return reversed_number

reverse_number(22)
```

3.  A quick google search says it easy to reverse a list using the `reversed` method
```python

def reverse_number(number):
  """
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  """
  string_number = str(number)
  list_string_number = list(string_number)
  reversed_list = reversed(list_string_number)
  #Reverse the number
  return reversed_number
```

4. Another google search tells me that I can turn a list into using the code:
`''.join(list)`
```python

def reverse_number(number):

  '''
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  '''
  string_number = str(number)
  list_string_number = list(string_number)
  reversed_list = reversed(list_string_number)
  reversed_string = ''.join(reversed_list)

  #Reverse the number
  return reversed_number
```

5. Finally I want to turn this back into a number
```python

def reverse_number(number):

  '''
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  '''
  string_number = str(number)
  list_string_number = list(string_number)
  reversed_list = reversed(list_string_number)
  reversed_string = ''.join(reversed_list)
  reversed_number = int(reversed_string)
  #Reverse the number
  return reversed_number
```

6. Turn into one line of code:
```python

def reverse_number(number):

  '''
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  '''
  reversed_number = int(''.join(reversed(list(str(number)))))

  return reversed_number
```
7. Write if statement for case when its negative (skip the first character, and then multiply by -1 after its a number again)
```python
def reverse_number(number):

  '''
  INPUT: a number that we want to reverse.
  OUTPUT: reversed number
  '''
    if str(n)[0] == '-':
        reversed_number = -1*int(''.join(reversed(str(n)[1:])))
    else:
        reversed_number = int(''.join(reversed(str(n))))
    return reversed_number
    ```
