class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """

    def containsDuplicate(self, nums):
        # Write your code here
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1
            else:
                dict[nums[i]] += 1
        for k, v in dict.items():
            if v > 1:
                return True
        return False
