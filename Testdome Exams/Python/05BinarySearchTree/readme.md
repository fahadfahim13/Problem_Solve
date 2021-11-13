## Binary Search Tree
**Binary search tree (BST)** is a binary tree where the value of each node is larger
or equal to the values in all the nodes in that node's left subtree and is
smaller than the values in all the nodes in that node's right subtree.
## Question
Write a function that, efficiently with respect to time used, checks if a given
binary search tree contains a given value. <br /> <br />
For example, for the following tree: <br />
    n1 (Value: 1, Left: null, Right: null) <br />
    n2 (Value: 2, Left: n1, Right: n3) <br />
    n3 (Value: 3, Left: null, Right: null) <br />
Call to `contains(n2, 3)` should `return True` since a tree with `root` at `n2` contains number 3.
```python
import collections
Node = collections.namedtuple('Node', ['left', 'right', 'value'])
def contains(root, value):
    pass
n1 = Node(value=1, left=None, right=None)
n3 = Node(value=3, left=None, right=None)
n2 = Node(value=2, left=n1, right=n3)
print(contains(n2, 3))
```