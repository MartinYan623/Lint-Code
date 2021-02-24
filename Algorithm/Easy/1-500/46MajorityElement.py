class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        length = len(nums)
        for i in range(int(length / 2) + 1):
            count = 1
            for j in range(i + 1, length):
                if nums[i] == nums[j]:
                    count += 1
            if count > length / 2:
                return nums[i]
