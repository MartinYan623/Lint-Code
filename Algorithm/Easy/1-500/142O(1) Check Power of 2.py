class Solution:
    """
    @param: n: An integer
    @return: True or false
    """

    def checkPowerOf2(self, n):
        # write your code here
        count = 0
        a = n
        for i in range(32):
            if a & 1:
                count += 1
            a = a >> 1
        if (count == 1 and n > 0) or (count == 2 and n <= 0):
            return True
        else:
            return False
