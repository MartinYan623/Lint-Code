class Solution:
    """
    @param: num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        # write your code here
        if num < 10:
            return num
        sum = 0
        while num >= 10:
            a = num / 10
            sum += a
            num = num - 10 * a
        sum += num
        if sum >= 10:
            sum = self.addDigits(sum)
        return sum
