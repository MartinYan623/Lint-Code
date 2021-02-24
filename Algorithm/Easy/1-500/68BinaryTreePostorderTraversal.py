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
    @return: Postorder in ArrayList which contains node values.
    """

    def __init__(self):
        self.__A = []

    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return self.__A

        lchild = root.left
        rchild = root.right
        self.postorderTraversal(lchild)
        self.postorderTraversal(rchild)
        self.__A.append(root.val)
        return self.__A
