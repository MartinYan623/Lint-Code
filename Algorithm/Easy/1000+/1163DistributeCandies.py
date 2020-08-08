class Solution:
    """
    @param candies: a list of integers
    @return: return a integer
    """

    def distributeCandies(self, candies):
        # write your code here
        unique_num = len(set(candies))
        get_num = int(len(candies) / 2)
        return min(unique_num, get_num)

