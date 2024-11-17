
def nodeDepthsHelper(node, depth):
    if node is None:
        return 0
    return depth + nodeDepthsHelper(node.left, depth + 1) + nodeDepthsHelper(node.right, depth + 1)



def nodeDepths(root):
    # Write your code here.
    return nodeDepthsHelper(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#init test cases
test = BinaryTree(1)
test.left = BinaryTree(2)
test.left.left = BinaryTree(4)
print(nodeDepths(test))