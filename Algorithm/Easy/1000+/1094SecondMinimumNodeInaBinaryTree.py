# use set property, we can store element first and then find the second minimum value.
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
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """

    def findSecondMinimumValue(self, root):
        # Write your code here
        uniques = set()
        self.collectvalue(root, uniques)
        m1, m2 = root.val, float('inf')
        print(uniques)
        for v in uniques:
            if m1 < v < m2:
                m2 = v
        return -1 if m2 == float('inf') else m2

    def collectvalue(self, root, uniques):
        if root:
            uniques.add(root.val)
            self.collectvalue(root.left, uniques)
            self.collectvalue(root.right, uniques)