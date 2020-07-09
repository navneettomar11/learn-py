class TreeNode:
    def __init__(self, val = 0, left = None, right = None ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.__dict__)

class BinaryTree:

    def __init__(self):
        self.root = None


    def add_tree_node(self, val, node: TreeNode) -> TreeNode:
       if node is None:
           node = TreeNode(val)
           return node

       if val < node.val:
         node.left = self.add_tree_node(val, node.left)

       if val > node.val:
           node.right = self.add_tree_node(val, node.right)

       return node



    def invert_binary_tree(self, node: TreeNode) -> TreeNode:
        if node.left is not None:
            self.invert_binary_tree(node.left)

        if node.right is not None:
            self.invert_binary_tree(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp

        return node


