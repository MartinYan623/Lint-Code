class Solution:
    """
    @param image: a 2-D array
    @param sr: an integer
    @param sc: an integer
    @param newColor: an integer
    @return: the modified image
    """
    def floodFill(self, image, sr, sc, newColor):
        # Write your code here
        row=len(image)
        col=len(image[0])
        temp=image[sr][sc]
        image[sr][sc]=newColor
        if sr-1>=0 and image[sr-1][sc]==temp:
            self.floodFill(image,sr-1,sc,newColor)
        if sc-1>=0 and image[sr][sc-1]==temp:
            self.floodFill(image,sr,sc-1,newColor)
        if sr+1<=row-1 and image[sr+1][sc]==temp:
            self.floodFill(image,sr+1,sc,newColor)
        if sc+1<=col-1 and image[sr][sc+1]==temp:
            self.floodFill(image,sr,sc+1,newColor)
        return image
