import sys
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        left = str(self.left) if self.left is not None else 'null'
        right = str(self.right) if self.right is not None else 'null'
        return "Val= "+str(self.val)+"[ Left "+ left +" Right "+right+" ]"


def create_tree_from_list(nums: List[int],root: TreeNode,  level: int, size: int) -> TreeNode:
    if level < size:
        root = TreeNode(nums[level])

        root.left = create_tree_from_list(nums, root.left,
                                     2 * level+ 1, size)

        root.right = create_tree_from_list(nums, root.right,
                                      2 * level + 2, size)
    return root



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


def preorder_traversal(node: TreeNode, pre_order_list: List[int]):

    if node is None:
        pre_order_list.append(None)
        return
    else:
        pre_order_list.append(node.val)

    preorder_traversal(node.left, pre_order_list)
    preorder_traversal(node.right, pre_order_list)

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    plist = []
    qlist = []
    preorder_traversal(p, plist)
    preorder_traversal(q, qlist)

    plen = len(plist)
    qlen = len(qlist)
    print(plist, qlist)
    if plen == 0 or qlen == 0 or plen != qlen :
        return False

    for i in range(0, plen):
        if plist[i] != qlist[i]:
            return False

    return True


def height(root: TreeNode) -> int:
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1

def zigzal_level_order(root: TreeNode) -> List[List[int]]:

    if root is None:
        return []

    current_level = []
    next_level = []

    ltr = True

    current_level.append(root)

    res = [ [] for i in range(height(root))]
    level = 0

    while len(current_level) > 0 :
        temp = current_level.pop(-1)
        if temp.val is not  None: res[level].append(temp.val)

        if ltr == True:
            if temp.left is not None: next_level.append(temp.left)
            if temp.right is not None: next_level.append(temp.right)
        else:
            if temp.right is not None: next_level.append(temp.right)
            if temp.left is not None: next_level.append(temp.left)

        if len(current_level) == 0:
            ltr = not ltr
            current_level, next_level = next_level, current_level
            level+=1


    return res

"""
Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal
"""
def build_tree_in_post_order(inorder: List[int], postorder: List[int]) -> TreeNode :


    def search(nums: List[int], start: int, end: int, target: int) -> int:
        i = start
        while i < end+1:
            if nums[i] == target:
                break
            i+=1
        return i

    def build_tree_helper(inord: List[int], postord: List[int], start: int, end: int, pindex: List[int]):
        if (start > end):
            return None

        node = TreeNode(postord[pindex[0]])
        pindex[0] -= 1

        if (start == end):
            return node

        iIndex = search(inorder, start, end, node.val)
        node.right = build_tree_helper(inord, postord, iIndex + 1,
                               end, pindex)
        node.left = build_tree_helper(inord, postord, start,
                              iIndex - 1, pindex)

        return node

    pindex= [len(postorder) -1]
    return build_tree_helper(inorder, postorder, 0, len(inorder)-1,  pindex )

if __name__ == "__main__":
   """
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    #root.left.left.left = TreeNode(6)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)

    width_of_binary_tree(root)
    """
   #p = TreeNode(1)
   #p.left = TreeNode(2)
   #p.right = TreeNode(3)

   #q = TreeNode(1)
   #q.left = TreeNode(None)
   #q.right = TreeNode(1)

   #print(is_same_tree(p, q))
   #root = None
   #root = create_tree_from_list([3,9,20,None,None,15,7],root, 0, 7)
   #root = create_tree_from_list([1,2,3,4,None,None,5],root, 0, 7)
   ##print(zigzal_level_order(root))

   print(build_tree_in_post_order([9,3,15,20,7], [9,15,7,20,3]))
