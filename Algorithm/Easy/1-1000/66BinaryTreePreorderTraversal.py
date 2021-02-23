"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def __init__(self):
        self.__A = []

    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.__A
        else:
            lchild = root.left
            rchild = root.right
            self.__A.append(root.val)
            self.preorderTraversal(lchild)
            self.preorderTraversal(rchild)
        return self.__A
