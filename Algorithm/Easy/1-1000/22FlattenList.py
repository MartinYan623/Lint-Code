class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer

    # Method 1
    def flatten(self, nestedList):
        # Write your code here
        result = []
        for item in nestedList:
            if type(item) is list:
                for subitem in self.flatten(item):
                    result.append(subitem)
            else:
                result.append(item)
        return result

    # Method 2
    def flatten2(self, nestedList):
        if type(nestedList) == int:
            return [nestedList]
        s = []
        result = []
        it = iter(nestedList)
        while True:
            try:
                t = next(it)
                if type(t) == int:
                    result.append(t)
                else:
                    s.append(it)
                    it = iter(t)
            except StopIteration:
                if len(s) == 0:
                    break
                it = s.pop()
        return result

# This is question to achieve the typical function flatten()
# Method1 uses the recursion and method2 uses iteration object (next method to get next one element in list)
