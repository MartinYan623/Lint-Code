class Solution:
    """
    @param ransomNote: a string
    @param magazine: a string
    @return: whether the ransom note can be constructed from the magazines
    """

    def canConstruct(self, ransomNote, magazine):
        # Write your code here
        dict1 = {}
        dict2 = {}
        for item in ransomNote:
            if item in dict1.keys():
                dict1[item] += 1
            else:
                dict1[item] = 1
        for item in magazine:
            if item in dict2.keys():
                dict2[item] += 1
            else:
                dict2[item] = 1
        for k, v in dict1.items():
            if k not in dict2.keys() or v > dict2[k]:
                return False
        return True
