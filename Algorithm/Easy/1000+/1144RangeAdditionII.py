class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """

    def maxCount(self, m, n, ops):
        # write your code here
        min_m = 40000
        min_n = 40000
        if len(ops) == 0:
            return m * n
        for num in range(len(ops)):
            m = ops[num][0]
            n = ops[num][1]
            if m < min_m:
                min_m = m
            if n < min_n:
                min_n = n
        return min_m * min_n
