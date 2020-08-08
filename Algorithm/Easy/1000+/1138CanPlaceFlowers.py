class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        for i in range(len(flowerbed)-1):
            if n==0:
                return True
            if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n=n-1
            elif flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n=n-1
        if n==0:
            return True
        else:
            return False