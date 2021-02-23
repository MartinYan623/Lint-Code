class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: An integer
    """

    def bitSwapRequired(self, a, b):
        # write your code here
        a = a ^ b
        count = 0
        for i in range(32):
            if a & 1:
                count += 1
            a = a >> 1
        return count
