class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def doubleFactorial(self, n):
        # Write your code here
        result=n
        n=n-2
        while n>0:
            result*=n
            n=n-2
        return result