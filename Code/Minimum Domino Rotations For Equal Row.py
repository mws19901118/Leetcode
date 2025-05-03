class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        dominos = [tops, bottoms]                                                                #Combine tops and bottoms as a 2D list.
        def count_rotations(row: int, target: int) -> int:                                       #Count the rotation needed to make given row all same as the start of target row.
            count = 0                                                                            #Initialize count.
            for x, y in zip(dominos[row], dominos[1 - row]):                                     #Traverse current row and opposite row together.
                if x == dominos[target][0]:                                                      #If current domino in the current row is already same as the start of target row, continue.
                    continue
                elif y == dominos[target][0]:                                                    #If current domino in the opposite row is the start of target row, rotatte.
                    count += 1
                else:                                                                            #Otherwise, cannot make current row all same as the start of target row, so return inf.
                    return inf
            return count                                                                         #Return count.
        result = min(count_rotations(i, j) for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)])         #Find the min rotation needed of 4 row and target combinations(2 rows and each row have 2 targets, start of self and start of opposite).
        return -1 if result == inf else result                                                   #Return -1 if result is inf, meaning no valid solution; otherwise, return result.
