class Solution:
    """
    @param nums: a list of integers
    @return: return a list of integers
    """
    def findDisappearedNumbers(self, nums):
        # write your code here
        a=set()
        b=set(nums)
        for i in range(1, len(nums)+1):
            a.add(i)
        return sorted(list(a-b))