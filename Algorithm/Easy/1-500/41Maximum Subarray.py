class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # write your code here
        length = len(nums)
        sum = 0
        ans = -10000
        for i in range(length):
            sum += nums[i]
            if sum > ans:
                ans = sum
            if sum < 0:
                sum = 0
        return ans
