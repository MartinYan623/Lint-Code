class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """

    def partitionArray(self, nums):
        # write your code here
        length = len(nums)
        for i in range(0, length, 1):
            if nums[i] % 2 != 0:
                pass
            else:
                for j in range(length, i + 1, -1):
                    if nums[j - 1] % 2 != 0:
                        temp = nums[i]
                        nums[i] = nums[j - 1]
                        nums[j - 1] = temp
                        length -= 1
                        break
