class Solution:
    """
    @param word: a string
    @return: return a boolean
    """
    def detectCapitalUse(self, word):
        # write your code here
        capitals=0
        if word.isupper() or word.islower() or (word.istitle() and word[1:].islower()):
            return True
        else:
            return False