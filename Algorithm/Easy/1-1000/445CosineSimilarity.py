class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: Cosine similarity
    """

    def cosineSimilarity(self, A, B):
        # write your code here
        length = len(A)
        molecule = 0
        donominator1 = 0
        donominator2 = 0
        fg = False
        for i in range(length):
            if (A[i] or B[i]) and fg == False:
                fg = True
            molecule += A[i] * B[i]
            donominator1 += A[i] * A[i]
            donominator2 += B[i] * B[i]
        if fg:
            ans = molecule / ((donominator1 ** 0.5) * (donominator2 ** 0.5))
            return ans
        else:
            return 2
