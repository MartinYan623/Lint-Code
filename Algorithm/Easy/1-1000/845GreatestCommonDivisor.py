class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """
    def gcd(self, a, b):
        # write your code here
        # return math.gcd(a,b)
        if a != 0:
            return self.gcd(b % a, a)
        else:
            return b