class Solution:
    """
    @param str: the str
    @return: the sum of bytes in the last word
    """
    def judgeTheLastNumber(self, str):
        # Write your code here
        i=0
        length=len(str)
        while length-i>1:
            if str[i]=='1':
                i+=2
            else:
                i+=1
        if len(str)-i==1:
            return 1
        else:
            return 2