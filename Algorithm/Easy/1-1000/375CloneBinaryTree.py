"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: root of new tree
    """

    def cloneTree(self, root):
        # write your code here
        if root is None:
            return None
        newroot = root
        newroot.val = root.val
        self.cloneTree(newroot.left)
        self.cloneTree(newroot.right)
        return newroot
