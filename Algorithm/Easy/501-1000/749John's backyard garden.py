class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """

    def isBuild(self, x):
        # Write your code here
        if x < 0:
            return "NO"
        if x % 3 == 0 or x % 7 == 0:
            return "YES"
        else:
            a = x - 3
            b = x - 7
            return self.isBuild(a) and self.isBuild(b)
