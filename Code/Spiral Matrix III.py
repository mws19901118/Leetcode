class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result, last = [[rStart, cStart]], [rStart, cStart]                  #Initialize result with starting point also initialize the last point.
        length = 2                                                           #Initialize length of spiral arm.
        while len(result) < rows * cols:                                     #Iterate while not all cells in matrix are visited.
            last[0] -= 1                                                     #Move last point one row up and one column right, so we don't have to explicitly do a move right.
            last[1] += 1
            for x, y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:                  #Traverse 4 directions: down, left, up, right.
                for _ in range(length):                                      #Move forward length times of current direction.
                    last[0] += x
                    last[1] += y
                    if 0 <= last[0] < rows and 0 <= last[1] < cols:          #If current point is inside matrix, copy last and append the copy to result.
                        result.append(last.copy())
            length += 2                                                      #Increase length by 2 to move to a larger spiral arm.
        return result
