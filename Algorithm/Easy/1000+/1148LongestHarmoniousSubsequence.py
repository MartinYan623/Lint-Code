class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """

    def findLHS(self, nums):
        # write your code here
        nums = sorted(nums)
        dict1 = {}
        for item in nums:
            if item in dict1.keys():
                dict1[item] += 1
            else:
                dict1[item] = 1
        count = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                if count < dict1[nums[i]] + dict1[nums[i + 1]]:
                    count = dict1[nums[i]] + dict1[nums[i + 1]]
        return count
