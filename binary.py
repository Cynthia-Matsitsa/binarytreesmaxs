class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postOrderTraversal(node):
    if node is None:
        return
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")

root = TreeNode('9')
node2 = TreeNode('2')
node3 = TreeNode('3')
node4 = TreeNode('4')
node5 = TreeNode('5')
node6 = TreeNode('6')
node7 = TreeNode('7')
node8 = TreeNode('8')

root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node7.left = node8

postOrderTraversal(root)