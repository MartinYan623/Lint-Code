class Solution:
    """
    @param s: a string
    @return: reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order
    """
    def reverseWords(self, s):
        # Write your code here
        answer=""
        word=s.split(' ')
        for i in range(len(word)):
            for j in range(len(word[i])-1,-1,-1):
                answer+=word[i][j]
            if i<len(word)-1:
                answer+=" "
        return answer
