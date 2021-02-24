class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """

    def generatePossibleNextMoves(self, s):
        # write your code here
        answer = []
        for i in range(len(s) - 1):
            temp = list(s)
            if s[i] == '+' and s[i + 1] == '+':
                temp[i] = '-'
                temp[i + 1] = '-'
                answer.append(''.join(temp))
        return answer
