class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        # write your code here
        i = 0
        while True:
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
            else:
                i += 1
