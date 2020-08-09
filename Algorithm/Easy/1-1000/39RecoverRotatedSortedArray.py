class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        # nums.sort()
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                for i in range(i+1, len(nums)):
                    nums.insert(0, nums.pop())
