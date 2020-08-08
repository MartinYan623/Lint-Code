class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        row=len(words)
        for i in range(row):
            string1=words[i]
            string2=""
            for j in range(row):
                string2+=words[j][i]
            if string1!=string2:
                return False
        return True