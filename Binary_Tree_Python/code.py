from BinaryTreeContinued import BinaryTreeContinued
from Trees import getTwoTree

if __name__ == '__main__':
    tree, tree2 = getTwoTree()
    # tree.inorder_loop(tree.root)
    # tree.preorder_iter(tree.root)
    # print()
    # tree.postorder_iter(tree.root)
    # print()
    # tree.mirror(tree.root)
    # tree.postorder(tree.root)
    # print()
    # tree.deleteTree(tree.root)
    # tree.inorder_loop(tree.root)
    print(tree.checkEqualTree(tree.root, tree2.root))