### Application of Sets

Another nice attribute of sets is that every value in a set is unique.  This means that if you are trying to get rid of duplicates in a list, an easy way to do this is as follows:

```python
list1 = [1,1,1,2,2,2,3,3,]
unique_list = list(set(list1))
```
This turns list1 into `[1,2,3]`

Below are some methods associated with sets

1. Add to a set:

```python
people = {"Richie", "Naren", "Sasha"}
people.add("Elliott")
```
The set is now `{"Richie", "Naren", "Sasha","Elliott"}`

2. Set unions

The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. For example, if `A = {1, 3, 5, 7}` and `B = {1, 2, 4, 6}` then `A ∪ B = {1, 2, 3, 4, 5, 6, 7}`.

```python
people = {"Richie", "Naren", "Sasha"}
vampires = {"Keenan", "Rohan"}
population = people.union(vampires)
```
Population is now: `{'Keenan', 'Naren', 'Richie', 'Rohan', 'Sasha'}`

This is the same as using the `|` operator:

```python
people = {"Richie", "Naren", "Sasha"}
vampires = {"Keenan", "Rohan"}
population = people | vampires
```

3. Set intersection

The intersection A ∩ B of two sets A and B is the set that contains all elements of A that also belong to B (or equivalently, all elements of B that also belong to A), but no other elements.

Form our example above, an intersect would return an empty set as there is no overlap between the values in our two sets.

4. Set difference

 Returns a set containing all the elements of invoking set but not of the second set. We can use ‘-‘ operator here.

 ```python
 people = {"Richie", "Naren", "Sasha"}
 vampires = {"Keenan","Sasha", "Rohan"}
 safe = people – vampires
 ```
Set `safe` will have all the elements that are in people but not vampire

5. Set operators

- `key in set` # containment check

- `key not in set` # non-containment check

- `s1 == s2` # set s1 is equivalent to set s2

- `s1 != s2` # set s1 is not equivalent to set s2

- `s1 | s2`  # the union of set s1 and set s2

- `s1 & s2` # the intersection of set s1 and set s2

- `s1 – s2` # the set of elements in s1 but not s2

- `s1 ˆ s2` # the set of elements in precisely one of s1 or s2
