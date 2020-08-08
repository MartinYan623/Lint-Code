class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        # Write your code here
        nums=sorted(nums)
        a = nums[-1]*nums[-2]*nums[-3]
        b = nums[0]*nums[1]*nums[-1]
        if a>b:
            return a
        else:
            return b
