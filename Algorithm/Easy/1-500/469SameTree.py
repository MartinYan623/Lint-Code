"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: a: the root of binary tree a.
    @param: b: the root of binary tree b.
    @return: true if they are identical, or false.
    """

    def isIdentical(self, a, b):
        # write your code here
        if a is None and b is None:
            return True
        elif a is None or b is None:
            return False
        elif a.val != b.val:
            return False
        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)
