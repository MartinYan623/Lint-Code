class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        if len(nums)==1:
            return ['Gold Medal']
        if len(nums)==2:
            if nums[0]>nums[1]:
                return ['Gold Medal','Silver Medal']
            else:
                return ['Silver Medal','Gold Medal']
        list1=sorted(nums)
        nums[nums.index(list1[-1])]='Gold Medal'
        nums[nums.index(list1[-2])]='Silver Medal'
        nums[nums.index(list1[-3])]='Bronze Medal'
        j=4
        for i in range(len(nums)-4,-1,-1):
             nums[nums.index(list1[i])]=str(j)
             j+=1
        return nums