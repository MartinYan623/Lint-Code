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
    @return: the minimum absolute difference between values of any two nodes
    """
    import sys
    def getMinimumDifference(self, root):
        # Write your code here
        nodeList = []
        self.inOrder(root, nodeList)
        k = sys.maxsize
        for i in range(1, len(nodeList)):
            k = min(k, nodeList[i] - nodeList[i - 1])
        return k

    def inOrder(self, root, nodeList):
        if root is None: return
        self.inOrder(root.left, nodeList)
        nodeList.append(root.val)
        self.inOrder(root.right, nodeList)