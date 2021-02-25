class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        length = len(nums)
        j = 0
        if length == 1 and nums[0] == 0:
            location = [0, 0]
            return location
        else:
            while j < length - 1:
                sum = 0
                for i in range(j, length):
                    sum = sum + nums[i]
                    if sum == 0:
                        location = [j, i]
                        return location
                j = j + 1
