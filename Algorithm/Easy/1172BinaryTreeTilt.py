"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the tilt of the whole tree
    """
    def findTilt(self, root):
        # Write your code here
        if root is None:
            return 0
        count = [0]
        self.helper(root, count)
        return count[0]

    def helper(self,root, count):
        if root is None:
            return 0
        left = self.helper(root.left, count)
        right = self.helper(root.right, count)
        count[0] += abs(left - right)
        return root.val + left + right