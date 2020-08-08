class Solution:
    """
    @param words: the given list of words
    @return: the number of different transformations among all words we have
    """
    def uniqueMorseRepresentations(self, words):
        # Write your code here
        table=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        code=[]
        for i in range(len(words)):
            subcode=""
            for item in words[i]:
                subcode=subcode+table[ord(item)-97]
            code.append(subcode)
        count=0
        for i in range(len(code)):
            flag=True
            for j in range(i+1,len(code)):
                if code[i]==code[j]:
                    flag=False
                    break
            if flag:
                count+=1
        return count