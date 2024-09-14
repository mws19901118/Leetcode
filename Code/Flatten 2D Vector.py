class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec                                                                            #Store the vec.
        self.indexX = 0                                                                           #Store the index for x coordinate.
        self.indexY = 0                                                                           #Store the index for y coordinate.
        self.advance()                                                                            #Move to next number.

    def advance(self):
        while self.indexX < len(self.vec) and self.indexY >= len(self.vec[self.indexX]):          #While self.indexX is valid and self.indexY reaches the end of self.vec[self.indexX], increase self.indexX and reset self.indexY to 0.
            self.indexX += 1
            self.indexY = 0

    def next(self) -> int:
        result = self.vec[self.indexX][self.indexY]                                               #Get result.
        self.indexY += 1                                                                          #Increase self.indexY.
        self.advance()                                                                            #Move to next number.
        return result

    def hasNext(self) -> bool:
        return self.indexX < len(self.vec) and self.indexY < len(self.vec[self.indexX])           #Return if self.indexX is valid and self.indexY is not at the end of self.vec[self.indexX].


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
