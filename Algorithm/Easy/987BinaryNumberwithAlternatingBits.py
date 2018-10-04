class Solution:
    """
    @param n: a postive Integer
    @return: if two adjacent bits will always have different values
    """
    def hasAlternatingBits(self, n):
        # Write your code here
        odd=0
        even=0
        while n:
            if n % 2 == 1:
                odd+=1
            else:
                even+=1
            if abs(odd-even)>1:
                return False
            n=n>>1
        return True