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
    @return: Inorder in ArrayList which contains node values.
    """

    def __init__(self):
        self.__A = []

    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.__A
        lchild = root.left
        rchild = root.right

        self.inorderTraversal(lchild)
        self.__A.append(root.val)
        self.inorderTraversal(rchild)
        return self.__A
