# reference link: https://blog.csdn.net/i_am_bird/article/details/78769566
class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def trailingZeroes(self, n):
        # write your code here
        count = 0
        while(n):
            n /= 5
            count += n
        return count