"""
A binary search tree is a binary tree that is ordered. This means that if you were to convert the tree to an array using an in-order traversal, the array would be in sorted order. The benefit gained by this ordering is that when the tree is balanced, searching is a logarithmic time operation, since each node you look at that isn't the one you're searching for lets you discard half of the tree.

If you haven't worked with binary trees before or don't understand what a traversal is, you can learn more about that here: https://www.codewars.com/kata/binary-tree-traversal.

In this kata, you will write a function that will validate that a given binary tree is a binary search tree. The sort order is not predefined so it should work with either.

These are valid binary search trees:
    5
  2   7
1  3    9

    7
  9   2

There are NOT valid BSTs:

   1
 2   3

    5
 2     9
   7

No test case will contain duplicate numbers
# bst invariant
# nodes on the left are less than equal to root and the right greater than equal to
# this is here for your documentation / type hints.
# the tests will use their own definition of T

output:
    so given a tree
    determine if its a BST in ascending order

traverse tree in-order traversal

iterate through the list starting index 1
if not(element[i] >= element[i -1])
    return false
return true
 1 2 3 5 7 9

if node.left.val < node.val < node.right.val

hmm lets look at invalid tree
  1
 2 3
 start at root




"""


class T:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_bst(node: T | None) -> bool:
    # your code here
    return False
