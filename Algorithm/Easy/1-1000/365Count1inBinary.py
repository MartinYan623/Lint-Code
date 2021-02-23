class Solution:
    """
    @param: num: An integer
    @return: An integer
    """

    def countOnes(self, num):
        # write your code here
        """
        count=0
        while num!=0:
            num = num & (num-1)
            count+=1
        return count
        """
        count = 0
        for i in range(0, 32):
            if num & 1:
                count = count + 1
            num = num >> 1
        return count
