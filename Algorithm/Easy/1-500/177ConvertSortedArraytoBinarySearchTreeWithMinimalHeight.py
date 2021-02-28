"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        length = len(A)
        if length == 0:
            return None
        else:
            mid = (length - 1) / 2
            root = TreeNode(A[mid])
            B = A[:mid]
            C = A[mid + 1:]
            root.left = self.sortedArrayToBST(B)
            root.right = self.sortedArrayToBST(C)
            return root
