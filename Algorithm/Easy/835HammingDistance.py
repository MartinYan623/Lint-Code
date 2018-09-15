class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        count=0
        xor=x^y
        while xor:
            if xor%2!=0:
                count+=1
            xor=xor>>1
        return count