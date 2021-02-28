class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        length = len(nums)
        nowlength = length
        for i in range(length - 1):
            while i < nowlength - 1 and nums[i] == nums[i + 1]:
                del nums[i + 1]
                nowlength -= 1
        ans = len(nums)
        return ans
