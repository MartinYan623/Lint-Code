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
    @return: the minimum difference between the values of any two different nodes in the tree
    """

    def minDiffInBST(self, root):
        nodeList = []
        self.inOrder(root, nodeList)
        k = sys.maxsize
        print(nodeList)
        for i in range(1, len(nodeList)):
            k = min(k, nodeList[i] - nodeList[i - 1])
        return k

    def inOrder(self, root, nodeList):
        if root is None: return
        self.inOrder(root.left, nodeList)
        nodeList.append(root.val)
        self.inOrder(root.right, nodeList)
