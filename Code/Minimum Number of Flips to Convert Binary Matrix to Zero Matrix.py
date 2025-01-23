class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])                                                #Get the dimensions.
        masks = [1 << (i * n + j) for i, j in product(range(m), range(n))]          #Assign a bit mask for each cell.
        result = m * n + 1                                                          #Initialize result to a large number.
        for b in range(1 << (m * n)):                                               #Traverse bit masks from 0 to 2 ** (m * n).
            count = 0                                                               #Count moves for current bit mask.
            board = deepcopy(mat)                                                   #Deepcopy mat.
            for i, mask in enumerate(masks):                                        #Traverse each mask.
                if b & mask:                                                        #If b & mask, perform a flip at the cell of current mask. 
                    count += 1                                                      #Increase count.
                    x, y = divmod(i, n)                                             #Restore the cell location.
                    board[x][y] ^= 1                                                #Flip it.
                    for u, v in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:   #Traverse 4 neighbors.
                        if 0 <= u < m and 0 <= v < n:                               #If neighbor is valid, flip it as well.
                            board[u][v] ^= 1
            if all(not board[i][j] for i, j in product(range(m), range(n))):        #If the final board is all 0, update result.
                result = min(result, count)
        return result if result < m * n + 1 else -1                                 #Return result if it is smaller than m * n + 1; otherwise, return -1.
