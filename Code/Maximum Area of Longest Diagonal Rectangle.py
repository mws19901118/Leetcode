class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        result, diagonal_square = 0, 0                                                          #Initialize result and max diagonal square.
        for x, y in dimensions:                                                                 #Traverse dimensions.
            square = x * x + y * y                                                              #Calculate current diagonal square.
            if square > diagonal_square or (square == diagonal_square and x * y > result):      #If it is greater than max diagonal sqaure or it equals max diagonal sqaure and the area is greater than result; update max diagonal square and result.
                diagonal_square = square
                result = x * y
        return result
