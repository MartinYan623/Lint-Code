class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    maxNum = -9999
    node = None

    def maxNode(self, root):
        # write your code here
        if root is None:
            return None
        self.max(root)
        return self.node

    def max(self, root):
        if root is None:
            return None
        if root.val > self.maxNum:
            self.maxNum = root.val
            self.node = root
        self.max(root.left)
        self.max(root.right)



