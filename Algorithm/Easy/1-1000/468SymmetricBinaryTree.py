"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """

    def isSymmetric(self, root):
        # write your code here
        if root == None:
            return True
        return self.helper(root.left, root.right)

    def helper(self, a, b):
        if a is None and b is None:
            return True
        if a and not b or not a and b:
            return False
        if a.val != b.val:
            return False
        return self.helper(a.left, b.right) and self.helper(a.right, b.left)