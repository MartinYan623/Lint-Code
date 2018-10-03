class Solution:
    """
    @param S:
    @return: nothing
    """
    def  toGoatLatin(self, S):
        #
        vowel=['a', 'e', 'i', 'o', 'u']
        words=S.split(' ')
        for i in range(len(words)):
            if words[i][0].lower() in vowel:
                words[i]+='ma'
            else:
                words[i]=words[i][1:len(words[i])]+words[i][0]
                words[i]+='ma'
            for j in range(i+1):
                words[i]+='a'
        sentence=""
        for i in range(len(words)):
            sentence+=words[i]
            if i != len(words)-1:
                sentence+=" "
        return sentence
