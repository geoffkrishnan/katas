"""
Nested List Depth
A nested list(array) is a list that appears as a value inside another list,

[item, item, [item, item], item]

The element at index 2 is the nested list.

Write a function that determines the depth of the deepest nested list within a given list.

return 1 if there are no nested lits. The list passed to your function can contain any data types.

A few examples.
list_depth([True])
return 1

list_depth([])
return 1

list_depth([2, "yes", [True, False]])
return 2

list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])
return 6

list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])
return 2
"""


def list_depth(lst):
    depths = []
    for element in lst:
        if isinstance(element, list):
            depths.append(list_depth(element) + 1)
    return max(depths) if depths else 1


list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1])  # 6
list_depth([True])  # 1
list_depth([])  # 1
list_depth([2, "yes", [True, False]])  # 2
list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]])  # 2
