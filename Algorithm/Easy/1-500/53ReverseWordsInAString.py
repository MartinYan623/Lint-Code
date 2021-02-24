class Solution:
    """
    @param: s: A string
    @return: A string
    """

    def reverseWords(self, s):
        # write your code here
        if s.strip() == "" or " " not in s:
            return s
        else:
            words = []
            for item in reversed(s.split()):
                words.append(item)
            return ' '.join(words)
