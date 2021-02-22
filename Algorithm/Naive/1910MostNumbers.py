class Solution:
    """
    @param array: An array.
    @return: An integer.
    """

    def findNumber(self, array):
        # Write your code here.
        count = {}
        for item in sorted(array):
            if item not in count.keys():
                count[item] = 1
            else:
                count[item] += 1
        return sorted(count.items(), key=lambda x: x[1], reverse=True)[0][0]
