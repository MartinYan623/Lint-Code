class Solution:
    """
    @param s: a string
    @param t: a string
    @return: the letter that was added in t
    """
    def findTheDifference(self, s, t):
        # Write your code here
        dict={}
        for i in range(len(s)):
            if s[i] not in dict:
                dict[s[i]]=1
            else:
                dict[s[i]]+=1
        print(dict)
        for i in range(len(t)):
            find=False
            for k,v in dict.items():
                if t[i]==k:
                    find=True
                    dict[k]=v-1
                if dict[k]<0:
                    return t[i]
            if find==False:
                return t[i]