class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        # write your code here
        length = len(nums)
        ans = 100000
        sum = 0
        for i in range(length):
            sum += nums[i]
            if sum < ans:
                ans = sum
            if sum > 0:
                sum = 0
        return ans
