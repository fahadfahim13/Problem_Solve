import collections


def contains(root, value):
    if root is None or value is None:
        return False
    if value == root.value:
        return True
    elif value > root.value:
        return contains(root.right, value)
    else:
        return contains(root.left, value)


def main():
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])
    n1 = Node(value=1, left=None, right=None)
    n3 = Node(value=3, left=None, right=None)
    n2 = Node(value=2, left=n1, right=n3)
    print(contains(n2, 3))


if __name__ == '__main__':
    main()
