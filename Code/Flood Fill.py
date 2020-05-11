class Solution:
    def fillPixels(self, image: List[List[int]], sr: int, sc: int, newColor: int, oldColor: int):
        m, n = len(image), len(image[0])
        if sr >= 0 and sr < m and sc >= 0 and sc < n and image[sr][sc] == oldColor and newColor != oldColor:  #If current coordinate is valid and current color is old color and old color is not the same as new color, start filling.
            image[sr][sc] = newColor                                                                          #Fill current pixel first, then 4 directions recursively.
            self.fillPixels(image, sr + 1, sc, newColor, oldColor)
            self.fillPixels(image, sr - 1, sc, newColor, oldColor)
            self.fillPixels(image, sr, sc + 1, newColor, oldColor)
            self.fillPixels(image, sr, sc - 1, newColor, oldColor)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.fillPixels(image, sr, sc, newColor, image[sr][sc])                                               #Fill pixels recursively.
        return image
