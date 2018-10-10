class Solution:
    """
    @param arr: the positions
    @return: minimum number of moves
    """
    def movingStones(self, arr):
        # Write your code here
        arr=sorted(arr)
        length=len(arr)
        i=0
        odd=[]
        even=[]
        while length>0:
            odd.append(abs(arr[i]-(2*i+1)))
            even.append(abs(arr[i]-2*(i+1)))
            length-=1
            i+=1
        return min(sum(odd),sum(even))