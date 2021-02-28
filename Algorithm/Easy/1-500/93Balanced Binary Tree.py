"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True
        a = self.treeHeight(root.left)
        b = self.treeHeight(root.right)
        if abs(a - b) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def treeHeight(self, root):
        if root is None:
            return 0
        else:
            lheight = self.treeHeight(root.left)
            rheight = self.treeHeight(root.right)
        return max(lheight, rheight) + 1
