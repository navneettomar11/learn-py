from unittest import TestCase

from leetcode.june_challenge import BinaryTree


class TestBinaryTree(TestCase):

    def setUp(self) -> None:
        self.binary_tree = BinaryTree()

    def test_add_tree_node(self) :

        root = self.binary_tree.add_tree_node(4, None)
        root = self.binary_tree.add_tree_node(2, root)
        root = self.binary_tree.add_tree_node(7, root)
        root = self.binary_tree.add_tree_node(1, root)
        root = self.binary_tree.add_tree_node(3, root)
        root = self.binary_tree.add_tree_node(6, root)
        root = self.binary_tree.add_tree_node(9, root)

        inverted_root = self.binary_tree.invert_binary_tree(root)
        print(inverted_root)






