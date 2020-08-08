class Solution:
    """
    @param n: an integer
    @return: if n is a power of three
    """

    def isPowerOfThree(self, n):
        # Write your code here
        if n == 0:
            return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n / 3
        return True

