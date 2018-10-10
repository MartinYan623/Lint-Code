class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        r=0
        l=0
        u=0
        d=0
        for i in range(len(moves)):
            if moves[i]=='R':
                r+=1
            if moves[i]=='L':
                l+=1
            if moves[i]=='U':
                u+=1
            if moves[i]=='D':
                d+=1
        if r==l and u==d:
            return True
        else:
            return False