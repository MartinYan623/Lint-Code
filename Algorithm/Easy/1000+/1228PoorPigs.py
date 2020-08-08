import math


# reference link: https://leetcode.com/problems/poor-pigs/discuss/94292/major-flaw-in-current-algorithm-fixed
class Solution:
    """
    @param buckets: an integer
    @param minutesToDie: an integer
    @param minutesToTest: an integer
    @return: how many pigs you need to figure out the "poison" bucket within p minutes
    """
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        # Write your code here
        if buckets==1:
            return 0
        else:
            n=minutesToTest/minutesToDie
            num_pigs=int(math.log(buckets/2,n))+1
        return num_pigs


    def poorPigs2(self, buckets, minutesToDie, minutesToTest):
        time = minutesToTest/minutesToDie + 1
        res = 0
        while(math.pow(time, res)< buckets):
            res=res+1

        return res

