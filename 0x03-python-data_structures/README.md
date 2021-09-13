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



