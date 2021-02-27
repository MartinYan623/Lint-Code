class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """

    def aplusb(self, a, b):
        # write your code here
        if a * b < 0 and abs(a) == abs(b):
            return 0
        else:
            while b != 0:
                sum = a ^ b
                carry = (a & b) << 1
                a = sum
                b = carry
            return a
