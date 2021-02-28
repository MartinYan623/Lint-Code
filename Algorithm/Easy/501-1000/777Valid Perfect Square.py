class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """

    def isPerfectSquare(self, num):
        # write your code here
        for i in range(1, int(num ** 0.5) + 1, 1):
            if num % (i ** 2) == 0 and num / (i ** 2) == 1:
                return True
        return False
