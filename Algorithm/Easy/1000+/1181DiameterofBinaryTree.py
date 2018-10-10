"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        if root is None:
            return 0
        return max(self.helper(root)-1,self.helper(root.left)+self.helper(root.right))

    # calculate the deepth of tree (nodes)
    # length of path = number of nodes - 1
    def helper(self,root):
        if root is None:
            return 0
        else:
            left=self.helper(root.left)
            right=self.helper(root.right)
            return max(left,right)+1
