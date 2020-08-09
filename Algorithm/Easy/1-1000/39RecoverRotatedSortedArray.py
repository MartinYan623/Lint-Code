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

# This question can be addressed by the direct function in Python sort()
# For other method, we first search the rotated point, and then use the method stack to pop the element one by one to insert into nums array