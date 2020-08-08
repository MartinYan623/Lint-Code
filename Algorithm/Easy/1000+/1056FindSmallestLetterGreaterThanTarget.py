class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """
    def nextGreatestLetter(self, letters, target):
        # Write your code here
        """
        target=ord(target)-97
        ordarray=[]
        min=999
        position=999
        for i in range(len(letters)):
            ordarray.append(ord(letters[i])-97)
            if ord(letters[i])-97>target and ord(letters[i])-97<min:
                min=ord(letters[i])-97
                position=i
        if min==999:
            return letters[ordarray.index(min(ordarray))]
        else:
            return letters[position]
        """
        for c in letters:
            if c>target:
                return c