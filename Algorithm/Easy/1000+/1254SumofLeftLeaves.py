"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        # Write your code here
        if not root:
            return 0
        sum = 0
        if root.left:
            left = root.left
            if not left.left and not left.right:# left leaves
                sum += left.val
            else:
                sum += self.sumOfLeftLeaves(left)
        if root.right:
            right = root.right
            sum += self.sumOfLeftLeaves(right)
        return sum