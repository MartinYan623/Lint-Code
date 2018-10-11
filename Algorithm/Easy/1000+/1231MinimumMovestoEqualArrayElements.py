class Solution:
    """
    @param nums: an array
    @return: the minimum number of moves required to make all array elements equal
    """
    def minMoves(self, nums):
        # Write your code here
        count = sum(nums) - len(nums) * min(nums)
        return count