class Solution:
    """
    @param s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        # write your code here
        if s is "":
            return 0
        l = s.split()
        length = len(l)
        return len(l[length - 1])
