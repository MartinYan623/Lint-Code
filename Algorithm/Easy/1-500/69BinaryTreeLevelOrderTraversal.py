"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # write your code here
        re = []
        if not root:
            return re
        re.append([root.val])
        li = [root]
        while True:
            ro = []
            va = []
            for node in li:
                if node.left:
                    ro.append(node.left)
                    va.append(node.left.val)
                if node.right:
                    ro.append(node.right)
                    va.append(node.right.val)
            if not va:
                return re
            re.append(va)
            li = ro
