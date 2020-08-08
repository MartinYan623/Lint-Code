class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """
    def findWords(self, words):
        # write your code here
        list1=['q','w','e','r','t','y','u','i','o','p']
        list2=['a','s','d','f','g','h','j','k','l']
        list3=['z','x','c','v','b','n','m']
        answer=[]
        for i in range(len(words)):
            count1=0
            count2=0
            count3=0
            for item in words[i]:
                if item.lower() in list1:
                    count1+=1
                if item.lower() in list2:
                    count2+=1
                if item.lower() in list3:
                    count3+=1
            if count1==len(words[i]) or count2==len(words[i]) or count3==len(words[i]):
                answer.append(words[i])
        return answer