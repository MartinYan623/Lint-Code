class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """

    def licenseKeyFormatting(self, S, K):
        # write your code here
        count = 0
        newstring = ''
        for item in S:
            if item != '-':
                count += 1
                newstring += item
        remainder = count % K
        if remainder == 0:
            answer = ''
        else:
            answer = newstring[:remainder].upper() + '-'
        if K == 1:
            for i in range(len(newstring)):
                answer += newstring[i].upper()
                if i != len(newstring) - 1:
                    answer += '-'
        else:
            for i in range(len(newstring) - remainder):
                answer += newstring[i + remainder].upper()
                if i % K == K - 1 and i != 0 and i != len(newstring) - remainder - 1:
                    answer += '-'
        return answer


