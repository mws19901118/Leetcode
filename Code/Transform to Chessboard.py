class Solution:
    def calculateMove(self, rowBinary: List[int], masks: List[int], target: int) -> int:
        moves, n = 0, len(rowBinary)                                                                                                                          #Initialize moves, dimension.
        xor, counterPartTarget = rowBinary[0] ^ target, sum(masks) ^ target                                                                                   #Find the difference between target and rowBinary[0] and the counter part target.
        for i in range(n):                                                                                                                                    #Apply xor on all rowBinary to transform rowBinary[0] to target.
            rowBinary[i] ^= xor
        moves = (bin(xor).count("1")) // 2                                                                                                                    #Count the moves so far; one move accounts for two 1 in xor.
        targetIndex, counterPartTargetCount = [i for i, x in enumerate(rowBinary) if x == target], sum(x == counterPartTarget for x in rowBinary)             #Find the indexes of all row binary eqauls to target now; also count the row binary eqauls to counter part target now.
        if not (len(targetIndex) == (n + 1) // 2 or len(targetIndex) == n // 2) or len(targetIndex) + counterPartTargetCount != n:                            #If the length of targetIndex is not (n + 1) // 2 or n // 2 or there is a row binary whose value is not target or counter part target, we cannot successfully transform board this way, so return n * n + 1.
            return n * n + 1
        if n % 2 == 1 and len(targetIndex) == (n + 1) // 2:                                                                                                   #If n is odd and len(targetIndex) == (n + 1) // 2, target must be put in even row.
            moves += sum(x % 2 != 0 for x in targetIndex)                                                                                                     #Count all row binary equals to target and not in even row; add count to moves cause we need to move them.
        elif n % 2 == 1 and len(targetIndex) != (n + 1) // 2:                                                                                                 #If n is odd and len(targetIndex) != (n + 1) // 2, target must be put in odd row.
            moves += sum(x % 2 == 0 for x in targetIndex)                                                                                                     #Count all row binary equals to target and not in odd row; add count to moves cause we need to move them.
        else:                                                                                                                                                 #If n is even, target can be put in either odd row or even row.
            moves += min(sum(x % 2 != 0 for x in targetIndex), sum(x % 2 == 0 for x in targetIndex))                                                          #Count the min value of all row binary equals to target in odd row or in even row; add count to moves cause we need to move them.
        return moves                                                                                                                                          #Return moves.
        
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)                                                                                                                                        #Get the dimension.
        masks = [1 << i for i in range(n)]                                                                                                                    #Compute the binary masks of each power of 2 from 1 to 2 ** (n - 1).
        targetOdd, targetEven = 0, 0                                                                                                                          #Since the chessboard doesnot have adjacent 0s or 1s. There can only be 2 patterns in each row, all odd indexes are 1 or all even indexes are 1.
        for i in range(n):                                                                                                                                    #Traverse n.
            if i % 2 == 0:                                                                                                                                    #Compute the pattern where all even indexes are 1.
                targetEven |= masks[i]
            else:                                                                                                                                             #Compute the pattern where are odd indexes are 1.
                targetOdd |= masks[i]
        rowBinary = [0] * n                                                                                                                                   #Initialize the binary int form of each row.
        for i in range(n):
            for j in range(n):
                rowBinary[i] |= masks[j] if board[i][j] else 0                                                                                                #Compute the binary int form of each row.
        count = (bin(rowBinary[0]).count("1"))                                                                                                                #Count the number of 1 in first row.
        result = n * n + 1                                                                                                                                    #Initialize result to be a really large value.
        if count == (n + 1) // 2:                                                                                                                             #If count == (n + 1) // 2, find the moves to transform board to chessboard with transforming first row to targetEven and update result if needed.
            result = min(result, self.calculateMove(deepcopy(rowBinary), masks, targetEven))
        if count == n // 2:                                                                                                                                   #If count == n // 2, find the moves to transform board to chessboard with transforming first row to targetOdd and update result if needed.
            result = min(result, self.calculateMove(deepcopy(rowBinary), masks, targetOdd))
        return -1 if result == n * n + 1 else result                                                                                                          #If result is still initial value, return -1; otherwise, return result.
