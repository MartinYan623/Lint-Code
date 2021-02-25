class Solution:
    """
    @param: : A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        i = len(nums)
        nums.sort()
        if i % 2 == 0:
            return (nums[int(i / 2) - 1])
        else:
            return (nums[int(i / 2)])
