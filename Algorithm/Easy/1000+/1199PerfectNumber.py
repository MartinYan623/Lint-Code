import math
class Solution:
    """
    @param num: an integer
    @return: returns true when it is a perfect number and false when it is not
    """
    def checkPerfectNumber(self, num):
        # write your code here
        i=1
        answer=1
        sqr = int(math.sqrt(num))
        if num==1:
            return False
        for i in range(2,sqr+1):
            if num % i == 0:
                answer+=i
                answer+=num/i
        if answer==num:
            return True
        else:
            return False