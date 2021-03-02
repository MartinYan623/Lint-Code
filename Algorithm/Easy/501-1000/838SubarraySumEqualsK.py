class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """

    def subarraySumEqualsK(self, nums, k):
        # write your code here
        count = 0
        for i in range(len(nums)):
            sub = 0
            for j in range(i, len(nums)):
                sub += nums[j]
                if sub == k:
                    count += 1
        return count

        count = 0
        dic = {0: 1}
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
            if (sub - k) in dic:
                count += dic[sub - k]
            if sub not in dic:
                dic[sub] = 1
            else:
                dic[sub] += 1
        return count
