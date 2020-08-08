class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels

    def numJewelsInStones(self, J, S):
        # Write your code here
        count=0
        for i in range(len(J)):
            count=count+S.count(J[i])
        return count
    """

    def numJewelsInStones(self, J, S):
        # Write your code here
        count = 0
        for i in range(len(J)):
            for j in range(len(S)):
                if J[i] == S[j]:
                    count += 1
        return count