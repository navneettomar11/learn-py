from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Val= "+str(self.val)


def find_level(root: TreeNode, level = 0):
    #print('1 ', root, level)
    if root is None:
        return  0

    downlevel = level
    leftlevel = righlevel = 0
    if root.left is not None:
        #print(root.left, level)
        leftlevel=find_level(root.left, level + 1)

    if root.right is not None:
        # print(root.right, level)
        righlevel=find_level(root.right, level + 1)

    #print('2 ', root, level, downlevel, leftlevel, righlevel)
    downlevel=max(leftlevel, righlevel) + 1
    return downlevel

def level_order_bottom_up(root: TreeNode) -> List[List[int]]:
    depth_level = find_level(root, 0)
    result = [ [] for i in range(0, depth_level)]
    if root.val is None:
        return result
    traversal(root, result, depth_level-1)
    return result

def traversal(node: TreeNode, tree: List[int], level: int) :

    if node.left is not None:
        traversal(node.left, tree, level-1)

    if node.right is not None:
        traversal(node.right, tree, level-1)

    tree[level].append(node.val)


if __name__ == "__main__":
    root = TreeNode(3,None, None)
    root.left = TreeNode(9, None, None)
    root.right = TreeNode(20, None, None)
    root.right.left = TreeNode(15, None, None)
    root.right.right = TreeNode(7,None,None)

    print(level_order_bottom_up(root))

    root = TreeNode(3, None, None)
    print(level_order_bottom_up(root))
