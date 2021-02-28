"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """

    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, left, right):
        if not left and not right:
            return True
        if left and not right or not left and right:
            return False
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)
