"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        # # write your code here
        # Method 1
        # MAX_DEPTH = 100000
        # count = 1
        # if root is None:
        #     return 0
        # if root.left is None and root.right is None:
        #     return 1
        # left_depth = MAX_DEPTH  if self.minDepth(root.left)==0 else self.minDepth(root.left)
        # right_depth = MAX_DEPTH if self.minDepth(root.right)==0 else self.minDepth(root.right)
        # if left_depth > right_depth:
        #     return right_depth + 1
        # else:
        #     return left_depth+ 1

        # Method 2
        if not root:
            return 0
        left_height = self.minDepth(root.left)
        right_height = self.minDepth(root.right)
        # 当前节点左子树或者右子树为空的情况下，至少有一个为0
        if not left_height or not right_height:
            return left_height + right_height + 1
        # 左右子树都不为空的情况
        else:
            return min(left_height, right_height) + 1
