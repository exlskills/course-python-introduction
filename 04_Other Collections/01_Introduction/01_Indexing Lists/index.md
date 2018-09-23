## Back to lists

One important aspect of lists that we have only briefly covered is indexing into lists.  Each value in a list has an index which refers to the location of the value inside the list.  For example if we have the following list:

```python
list1 = [1,2,3,4]
```
To access the value = 1, we could use the fact that we know it is at the 0th index. This means `list1[0]` will give the value = 1.  This works for each value in the array and as you can see in this specific list, our indexes go from 0 to 3.  

If you want to access the last value in the list (4) we could either use the index of `3` OR we could use backwards indexing.  That means that to get the last value in any list, we could say `list1[-1]`.  Seems a little confusing, but you will get the hang of it real quick.  This backwards indexing can be generalized, and you can access the second to last index using -2 and so on.
