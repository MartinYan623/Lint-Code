class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        """
        if num ==0 :
            return False
        while num!=1:
            if num % 4 !=0:
                return False
            num = num / 4
        return True
        """
        return num > 0 and (num & (num -1)) == 0 and (num & 0x55555555) != 0