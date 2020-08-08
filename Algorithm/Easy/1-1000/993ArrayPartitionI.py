class Solution:
    """
    @param nums: an array
    @return: the sum of min(ai, bi) for all i from 1 to n
    """
    def arrayPairSum(self, nums):
        # Write your code here
        length=len(nums)
        n=int(length/2)
        nums=sorted(nums)
        sum=0
        for i in range(n):
            sum+=min(nums[2*i],nums[2*i+1])
        return sum