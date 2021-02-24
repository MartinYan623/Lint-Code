class Solution:
    """
    @param: nums: an integer array
    @return:
    """

    def moveZeroes(self, nums):
        # write your code here
        length = len(nums)
        for i in range(length):
            if nums[i] == 0:
                j = i
                while nums[j] == 0 and j < length - 1:
                    j += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        return nums
