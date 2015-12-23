class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d                                                              #Store the 2d vector.
        self.row = 0                                                                    #Record the index of current row.
        self.column = 0                                                                 #Record the index of current column.

    def next(self):
        """
        :rtype: int
        """
        temp = self.vec2d[self.row][self.column]                                        #Get the value.
        self.column += 1                                                                #Update current index of column.
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row != len(self.vec2d) and self.column == len(self.vec2d[self.row]): #If current element reaches the end of current row, go to the next row.
            self.row += 1
            self.column = 0
        return self.row != len(self.vec2d)                                              #If current row equals to the length of 2d vector, return false; otherwise, return true.

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
