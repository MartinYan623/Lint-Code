class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """
    def isPowerOfTwo(self, n):
        # Write your code here
        while n>1:
            n=n/2
        if n ==1:
            return True
        else:
            return False