class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """

    def reverseInteger(self, number):
        # write your code here
        l = []
        while (number > 0):
            l.append(number % 10)
            number = number // 10
        return l[0] * 100 + l[1] * 10 + l[2]
