"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """

    def tree2str(self, t):
        # write your code here
        result = ""
        if t is None:
            return ''
        result += str(t.val)
        if t.left is not None and t.right is None:
            result = result + '(' + self.tree2str(t.left) + ')'
        if t.left is None and t.right is not None:
            result = result + '()(' + self.tree2str(t.right) + ')'
        if t.left is not None and t.right is not None:
            result = result + '(' + self.tree2str(t.left) + ')'
            result = result + '(' + self.tree2str(t.right) + ')'
        return result
