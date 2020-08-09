class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """

    # Method 1
    def rotateString(self, s, offset):
        # write your code here
        if len(s) == 0 or offset == 0:
            return s
        n = offset % len(s)
        ss = s + s
        ss = ss[len(s) - n:2 * len(s) - n]
        for i, x in enumerate(ss):
            s[i] = x

    # Method 2
    def rotateString2(self, s, offset):
        if len(s) == 0 or offset == 0:
            return s
        for i in range(offset % len(s)):
            s.insert(0, s.pop())

