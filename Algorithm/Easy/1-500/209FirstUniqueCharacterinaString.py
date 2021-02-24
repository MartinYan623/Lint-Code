class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """

    def firstUniqChar(self, str):
        # Write your code here
        dict1 = {}
        for item in str:
            if item in dict1.keys():
                dict1[item] += 1
            else:
                dict1[item] = 1
        for k, v in dict1.items():
            if v == 1:
                return k

