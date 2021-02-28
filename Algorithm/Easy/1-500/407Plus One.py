class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """

    def plusOne(self, digits):
        # write your code here
        length = len(digits)
        num = 0
        for i in range(length):
            num += digits[i] * (10 ** (length - i - 1))
        num += 1
        l = []
        while num:
            l.append(num % 10)
            num = num / 10
        l.reverse()
        return l
