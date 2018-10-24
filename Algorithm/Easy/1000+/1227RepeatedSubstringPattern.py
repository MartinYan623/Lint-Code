class Solution:
    """
    @param s: a string
    @return: return a boolean
    """

    def repeatedSubstringPattern(self, s):
        # write your code here
        tmp = s[1:] + s[:-1]
        return (tmp.find(s) != -1)


    def repeatedSubstringPattern(self, s):

        size = len(s)
        for x in range(1, int(size / 2 + 1)):
            if size % x:
                continue
            if s[:x] * (int(size / x)) == s:
                return True
        return False
