class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        # Write your code here
        p=[]
        dict1={}
        for i in range(len(B)):
            if B[i] in dict1.keys():
                dict1[B[i]].append(i)
            else:
                dict1[B[i]]=[i]
        for i in range(len(A)):
            p.append(dict1[A[i]][-1])
        return p
