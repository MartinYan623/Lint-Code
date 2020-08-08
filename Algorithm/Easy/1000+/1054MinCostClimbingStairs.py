class Solution:
    """
    @param cost: an array
    @return: minimum cost to reach the top of the floor
    """

    def minCostClimbingStairs(self, cost):
        # Write your code here
        length = len(cost)
        dp = []
        dp.append(0)
        dp.append(0)
        for i in range(2, length + 1):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
        return dp[length]

