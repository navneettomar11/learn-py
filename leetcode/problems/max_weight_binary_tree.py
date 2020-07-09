import sys

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return "Val= "+str(self.val)


def width_of_binary_tree(root: TreeNode) -> int:
    map = {}
    res = 1
    preorder(root, 0, 1, map)
    for level in map:
        rec = map.get(level)
        print(level, rec)
        res = max(res, rec[1] - rec[0] + 1)

    print(res)



def preorder(node: TreeNode, level: int, pos: int, map):
    if node is None:
        return
    rec = map.get(level, None)
    if rec is None:
        rec = [sys.maxsize,-1* sys.maxsize -1]

    rec[0] = min(rec[0], pos)
    rec[1] = max(rec[1], pos)
    map[level] = rec
    preorder(node.left, level + 1, 2*pos, map)
    preorder(node.right, level + 1, 2*pos + 1, map)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    #root.left.left.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)

    width_of_binary_tree(root)
