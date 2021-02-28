class Solution:
    """
    @param: nums: An integer array sorted in ascending order
    @param: target: An integer
    @return: An integer
    """

    def findPosition(self, nums, target):
        # write your code here
        length = len(nums)
        end = length - 1
        start = 0
        location = (end - start) / 2
        while start < end:
            if target < nums[location]:
                end = location - 1
                location = (end - start) / 2
            elif target > nums[location]:
                start = location + 1
                location = (end + start) / 2
            else:
                return location
        return -1
