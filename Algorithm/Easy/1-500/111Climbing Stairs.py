class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        """
        if n==0 or n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        """
        a = []
        a.append(1)
        a.append(1)
        for i in range(2, n + 1, 1):
            a.append(a[i - 1] + a[i - 2])
        if n == 0:
            return 0
        else:
            return a[n]


class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        # write your code here
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
