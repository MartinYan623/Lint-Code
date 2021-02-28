class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        length = len(nums)
        if length == 0:
            return 0
        i = 0
        while i < length - 1:
            count = 1
            while i < length - 1 and nums[i] == nums[i + 1]:
                count += 1
                if count > 2:
                    del nums[i + 1]
                    count -= 1
                    length -= 1
                else:
                    i += 1
            i += 1
        ans = len(nums)
        return ans
