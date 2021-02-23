class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        length = len(nums)
        start = 0
        end = length
        mid = (end - start) / 2
        while start <= end:
            if nums[mid] < target:
                start = mid + 1
                mid = (end + start) / 2
            elif nums[mid] > target:
                end = mid - 1
                mid = (end - start) / 2
            else:
                while nums[mid] == target:
                    mid -= 1
                return mid + 1
        return -1
