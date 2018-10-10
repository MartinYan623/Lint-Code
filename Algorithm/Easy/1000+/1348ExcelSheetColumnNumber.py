class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def titleToNumber(self, s):
        # write your code here
        length=len(s)
        answer=0
        for i in range(length):
            answer+=(ord(s[i])-64)*pow(26,length-i-1)
        return answer
