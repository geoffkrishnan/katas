"""
A perfect binary tree is a binary tree in which all interior nodes have two children and all leaves have the same depth or same level.

You are given a class called TreeNode. Implement the method isPerfect which determines if a given tree denoted by its root node is perfect.

Note: TreeNode class contains helper methods for tree creation, which might be handy for your solution.

Feel free to update those methods, but make sure you keep their signatures intact (since they are used from within test cases).

You can (and should) add more tests to validate your solution, since not all cases are covered in the example test cases.


So is perfect == balanced?

No. Balanced is when height diff between subtrees is exactly 1

All perfect is balanced but not all balanced is perfect


So every node has to have two children. only edge case is root node by itself [1] that is considered perfect.

So every node you add after root must be in multiples of 2
size of a perfect binary tree is fixed then.
with 1 level, 1 node
2 levels 1 + 2
3 levels 1 + 2 + 4
4 levels 1 + 2 + 4 + 8

since levels MUST be equal, BFS the most sense here to me and do like level order traversal verifying levels are equal and as soon as a level isn't equal can return false

have to do DFS tho.

alr se given a perfect tree let me just raw dfs and see how im actually traversing
         1
      2     3
     4 5   6 7

dfs on 1
dfs(1.left) called
    dfs(2.left)
    dfs(2.right)

dfs(1.right) called
    dfs(3.left)
    dfs(3.right)

1 2 4 5 3 6 7

ok so the left subtree of root has to finish traversing before the right subtree of root

so can try to assert if fullness of left subtree == right subtree?

not exactly tho. like the left subtree itself has to be properly full. and then need to compare with right subtree

but its not just if left subtree is equal to right subtree directly because both can be not full and equal each other

how do I actually determine if a subtree is full? what does it mean for subtree to be full.

if a node has both left and right children that it is a full node.

ok. so when i  call dfs(node.left) and dfs(node.right) and both those calls do not return none THEN the node that i called that one MUST be full?

but what about leaf nodes?

leaf node has no children.

we're already saying tahat returning none means something in checking fullness

so we need to return something else to indicate leafness

maybe return True


wait so have to also keep track of level in the dfs

so need to do the subtree validation, leaf check and keep track of level height.

then if both subtrees are good and they're the same level then its perfect.

already know how to do the level height thing, have to do return 1 every time go deeper else leaf return 0

pseudocode:
base case
    is a leaf
    if node.left none and node.right none:
        return 0(didn't go deeper so height not incrementing
    if node.left and node.right(full node)
        get left subtree height
        get right subtree height
        if left == -1 or right == -1 or left != right
            return -1
    return -1(means only one child not full node so need some way to represent that)

    so if -1 is never returned must be a perfect tree

"""


class TreeNode:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def is_perfect(tree: TreeNode) -> bool:
    def dfs(node):
        if not node.left and not node.right:
            return 0
        if node.left and node.right:
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            if left_height == -1 or right_height == -1 or left != right:
                return -1
            return left_height + 1
        return -1

    return dfs(tree) != -1
