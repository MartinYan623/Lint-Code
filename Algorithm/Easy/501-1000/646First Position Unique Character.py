class Solution:
    """
    @param: s: a string
    @return: it's index
    """

    def firstUniqChar(self, s):
        # write your code here
        length = len(s)
        for i in range(length):
            j = 0
            fg = True
            while j < length:
                if s[i] == s[j] and i != j:
                    fg = False
                    break
                j += 1
            if fg:
                return i
        return -1
