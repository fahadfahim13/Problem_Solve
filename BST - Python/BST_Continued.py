from BST import BST


class BST_Continued(BST):
    def existPair(self, node, sum):
        if node is None:
            return False
        if self.search(node, sum - node.value):
            return True
        else:
            return self.existPair(node.left, sum) or self.existPair(node.right, sum)

    def existPairWithSet(self, node, sum, set):
        if node is None:
            return False
        if str(sum - node.value) in set:
            return True
        else:
            set[str(node.value)] = 1
            return self.existPairWithSet(node.left, sum, set) or self.existPairWithSet(node.right, sum, set)


if __name__ == '__main__':
    data = [8, 3, 6, 10, 4, 7, 1, 14, 13]
    tree = BST_Continued()
    root = tree.insert(None, data[0])
    for i in range(1, len(data)):
        tree.insert(root, data[i])

    print(tree.existPair(root, 100))
    print(tree.existPairWithSet(root, 100, {}))