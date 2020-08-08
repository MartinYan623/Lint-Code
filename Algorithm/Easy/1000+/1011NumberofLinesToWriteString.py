# math.ceil()向上取整 math.floor()向下取整  //截断取整
class Solution:
    """
    @param widths: an array
    @param S: a string
    @return: how many lines have at least one character from S, and what is the width used by the last such line
    """
    def numberOfLines(self, widths, S):
        # Write your code here
        line=1
        units=0
        for i in range(len(S)):
            if units+widths[ord(S[i])-97]<=100:
                units=units+widths[ord(S[i])-97]
            else:
                units=widths[ord(S[i])-97]
                line+=1
        return [line,units]