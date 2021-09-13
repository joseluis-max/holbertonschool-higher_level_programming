# LISTS
__What is a list ?__

List in python is a compound data type, used to group together other values generally the same type data, every value is separate by `,`, inner on square brackets.
``` python
>>>squares = [1, 3, 5, 9]
```

- [x] We can make concatenation
- [x] List are a mutable type
- [x] List can be indexed and sliced

__List data type methods__

| Name | Description |
|---   |---          |
| append | Add an item to the end of the list|
| extend | appending all the items from the iterable item in end of the list|
| insert | Insert an item at a given position `list.insert(i, x)`|
| remove | Remove first item whose value equial to x `list.remove(x)`|
| por | Remove item at the given position and return it, if index no is specified remove the last item `list.pop(i)`|
| clear | Remove all items |
| index | Return zero-based index in the list of the first item whose value is equal to x |
| count | Return the number of times x appers in the list `list.count(x)` |
| sort | Sort items of the list in place |
| reverse | Reverse the elements of the list in place |
| copy | Return a shadow copy of the list |

  
> **_NOTE:_** You can use list as Stacks (last-in, first-out) with the methods `append()` and `pop()`

> **_NOTE:_** You can use list as Queues (first-in, first-out) with `collection.deque` and methods `append()` and `popleft()`

``` python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
__List Comprehensions__

Provide a consise way to create lists.
Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

> **__NOTE:__** A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.

``` python
>>> squeare = [x**2 for x in range(10)]
    squeare [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

- [x] We can make concatenation
- [x] List are a mutable type
- [x] List can be indexed and sliced

__The del statement__

Remove a item from a list given its index instead of its value, can also be used to remove slices from a list or clear entire list, or delete entire variables

``` python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
>>> del a
```

__Tuples and Sequences__

Is a number of values separated by commas.
Tuples are immutable, and usually contain a heterogeneous sequence of elements that are accessed via unpacking or indexing (or even by attribute in the case of namedtuples)

``` python
>>> t = 12345, 54321, 'hello!'
>>> t2 = (12345, 54321, 'hello!')
>>> # empty tuple
>>> empty = ()
>>> # single element
>>> singleton = 'Hola',                           # <-- note trailing comma
```
- [x] Tuples may be nested
- [x] Tuples are inmutable
- [x] Tuples can contain mutable objects
