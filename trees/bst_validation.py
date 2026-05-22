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
# nodes on the left are less than equal to node and the right greater than equal to
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

why is this invalid
nodes left is greater and rooots right is also greater

so if node.left >= node then check if node.right <= node
if node.right >= node then check if node.left <= node


    5
 2     9
   7

why is this one invalid?
I believe it is because of 7?
since 7 is greater than 5 it should go to 5.right and then end up on 9.left I think

Actually it's because EVERY node on the left subtree from the node MUST be less than the node. 7 is on left but is greater

Ok.

so when you perform in-order traversal on a BST, you get an ascending or descending monotonic sequence.


So as you're performing the in-order traversal, as long as the next node you get follows that property, BST holds true as soon as it DOESN'T you can immediately return false

In-order traversal(i just looked it up)
left, node, right recursively

How do you determine if the BST is in ascending vs descending? Can infer from the first two nodes.
If first node is LESS than second node, can assume ascending else descending
input guaranteed no duplicate nums so can't have first node == second node. interesting edge case to work around maybe. what if u jsut have all dupes. lol.


in-order traversal:
    goal - Get the nodes in order from leftmost to rightmost.

    how?
    - if we need to start with leftmost node, then need to do depth-first search down the tree to the leftmost node.
    - THEN from the leftmost, need to go right to the next leftmost? like. the next node after the leftmost will be the parent of the leftmost.
    - Then we want the right child.
    we want to do this for the entire leftsubtree.

    THEN once the left subtree is done, we go node, then the right sutree.

    in the right subtree, the same process follows. go down and to the left until you hit the bottom. and then back up to parent then right.


    so left, node, right

so start node.left until none is hit.
node.left needs to be called recursively base case being None?

in_order(node):
    if node is None:
        return
    in_order(node.left)
    in_order(node)
    in_order(node.right?)

when are the nodes processed. need to process AFTER going down as deep as possible. left node and right

fuck man i don't get it.

okay. so given a tree
      5
 2        9
   7

the result i want is 2 7 5 9

i want to print the LEFT MOST node so once i call the function on node. i need to go to left most. how do i get there from node

5.left = 2
2.left = None
ok now I return from that back at 2
I need to print 2. so im currently at 2 so i can just print node.val

then i want to print 7
so 2.right im at 7
im recursing the same thing so i need to do 7.left?

7.left returns None back to 7

print 7
then 7.right returns none back to 7
now what. i need to go back to 5 somehow

5 -> 2 -> 7(im here)
so return again from 7 but what do i return? nothing?
then back to 2 return
now im at 5. but from 5's perspective i just finished doing 5.left
so now i print 5 and do 5.right

5.right -> 9
and then i can do the same 9.left none and 9.right none back to 9 print 9 and then return
and then im at 5 return and im  done
pseudocode:
    def inorder(node):
        if node is none:
            return
        inorder(node.left)
        print(node)
        inorder(node.right)
        return

Okay. So I understand how to do inorder traversal.

How do I modify this to like return False when sequence isn't monotonic

So. what do I need to identify that?
I need to check the CURRENT val vs the previous value. so I need the previous value. or that previous value needs to be passed down?

      5
 2        9
   7

okay. so i go to 2
im at 2. then the next one is 2.right which is 7
at 7 i need to check

is node.val less than 2 or greater than 2

if its less than 2 i need to like set a boolean flag(ascending = False) if its greater than 2 then ascending = True?

in this case 7 > 2 so ascending = True

then i go to 5
at 5 i need 7
is 5 > 7. false so return False and stop recursing.

so i need to like pass the value upwards i want to return the value?

what happens if i return the value. it fucks up the recursive function tho..

i don't understand how to do this part

i need like node.prev but its a not doubly linked list so i don't have node.prev

just need to store it in variable i guess.

but need to modify it. can't do with int, tried already, each new function call creates its own copy of the variable

can use list outside function to store, each new function call references the same list object so that works

so prev = []

"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def in_order(node) -> None:
    if node is None:
        return
    in_order(node.left)
    print(node.val)
    in_order(node.right)
    return


root = Node(5, Node(2, None, Node(7)), Node(9))

in_order(root)


def is_bst(root: Node) -> bool:
    if root is None or (root.left is None and root.right is None):
        return True

    prev = []

    def check_ascending_or_descending(node):
        if len(prev) == 2 or node is None:
            return
        check_ascending_or_descending(node.left)
        if len(prev) < 2:
            prev.append(node.val)
        check_ascending_or_descending(node.right)

    check_ascending_or_descending(root)

    ascending = [False]
    if prev[0] < prev[1]:
        ascending[0] = True

    def check_tree(node):
        if node is None:
            return True

        if not check_tree(node.left):
            return False

        if ascending[0] and prev[0] > node.val:
            return False
        if not ascending[0] and prev[0] < node.val:
            return False

        prev[0] = node.val

        if not check_tree(node.right):
            return False

        return True

    return check_tree(root)


test = Node(1, Node(2), Node(3))
test2 = Node(5, Node(2, Node(1), Node(3)), Node(7, None, Node(9)))
test3 = Node(7, Node(9), Node(2))
test4 = Node(5, Node(2, None, Node(7)), Node(9))
test5 = Node(42)
test6 = None
test7 = Node(1, None, Node(2))
test8 = Node(2, None, Node(1))
tests = [test, test2, test3, test4, test5, test6, test7, test8]

for test in tests:
    print(is_bst(test))
