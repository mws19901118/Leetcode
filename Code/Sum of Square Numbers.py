class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root = floor(sqrt(c))                               #Calculate the floor of root of c.
        squares = set([i * i for i in range(root + 1)])     #Put the square numbers from 0 to root in a set.
        return any(c - x in squares for x in squares)       #Return if any c - x in squares for each x in squares.
