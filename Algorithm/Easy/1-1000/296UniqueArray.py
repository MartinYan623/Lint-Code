class Solution:
    """
    @param arr: a integer array
    @return: return the unique array
    """

    def getUniqueArray(self, arr):
        # write your code here
        # new = []
        # for item in arr:
        #     if item not in new:
        #         new.append(item)
        # return new

        return list(dict.fromkeys(arr))
