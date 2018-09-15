class Solution:
    """
    @param n: an unsigned integer
    @return: the number of 1 bits
    """
    def hammingWeight(self, n):
        # write your code here
        count=0
        while n:
            if n%2!=0:
                count+=1
            n=n>>1
        return count