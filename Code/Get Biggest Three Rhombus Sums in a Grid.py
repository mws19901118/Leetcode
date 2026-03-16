class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        def addToHeap(rhombusSum: int) -> None:                                                            #Add a rhombus sum to heap if it is not already seen.
            if rhombusSum not in seenSum:
                seenSum.add(rhombusSum)
                heappush(heap, rhombusSum)
                if len(heap) > 3:                                                                          #Pop heap if its size is greater than 3.
                    heappop(heap)

        def calculateSum(x: int, y: int, l:int, isDiagonal: bool) -> int:                                  #Calculate sum from coordinate x, y to l steps forward based on its diagonal or reverse diagonal.
            if isDiagonal:
                start = (x - y, 0) if x >= y else (0, y - x)                                               #Calculate the starting point of the diagonal.
                index = y - start[1]                                                                       #Calculate the index of (x, y) in the prefix sum of the diagonal.
                return diagonals[start][index + l + 1] - diagonals[start][index]                           #Return the range of sum.
            else:
                start = (m - 1, x - (m - 1 - y)) if x >= m - y else (x + y, 0)                             #Calculate the starting point of the reverse diagonal.
                index = y - start[1]                                                                       #Calculate the index of (x, y) in the prefix sum of the reverse diagonal.
                return reverseDiagonals[start][index + l + 1] - reverseDiagonals[start][index]             #Return the range of sum.

        m, n = len(grid), len(grid[0])                                                                     #Get the dimensions.
        seenSum = set()                                                                                    #Store seen rhombus sums.
        heap = []                                                                                          #Use a min heap to store top 3 largest rhombus sums.
        diagonals, reverseDiagonals = defaultdict(lambda: [0]), defaultdict(lambda: [0])                   #Store the prefix sum of each diagonal and reverse diagonal.
        for i in range(m + n - 1):                                                                         #Enumerate each diagonal.
            x, y = (i, 0) if i < m else (0, i - m + 1)                                                     #Calculate the starting coordinate.
            u, v = x, y
            while u < m and v < n:                                                                         #Traverse current diagonal and populate the prefix sum.
                diagonals[(x, y)].append(diagonals[(x, y)][-1] + grid[u][v])
                u += 1
                v += 1
        for i in range(m + n - 1):                                                                         #Enumerate each reverse diagonal.
            x, y = (i, 0) if i < m else (m - 1, i - m + 1)                                                 #Calculate the starting coordinate.
            u, v = x, y
            while u >= 0 and v < n:                                                                        #Traverse current reverse diagonal and populate the prefix sum.
                reverseDiagonals[(x, y)].append(reverseDiagonals[(x, y)][-1] + grid[u][v])
                u -= 1
                v += 1
        for i, j in product(range(m), range(n)):                                                           #Traverse the grid.
            addToHeap(grid[i][j])                                                                          #Add current cell value to heap as itself is a rhombus.
            l = 1
            while j + 2 * l < n and i + l < m and i - l >= 0:                                              #Fix current cell as the left corner, then enunerate the length(excluding starting point) of edge while the rhombus is value.
                s = 0                                                                                      #Initialize sum.
                s += calculateSum(i, j, l, True)                                                           #Add the edge sum from left corner to botton corner.
                s += calculateSum(i, j, l, False)                                                          #Add the edge sum from left corner to top corner.
                s += calculateSum(i - l, j + l, l, True)                                                   #Add the edge sum from top corner to right corner.
                s += calculateSum(i + l, j + l, l, False)                                                  #Add the edge sum from bottom corner to right corner.
                s -= grid[i][j] + grid[i - l][j + l] + grid[i + l][j + l] + grid[i][j + 2 * l]             #Deduct the sums at 4 corners as they are adeed twice.
                addToHeap(s)                                                                               #Add the sum to heap.
                l += 1                                                                                     #Increase length.
        return sorted(heap, reverse = True)                                                                #Sort the heap in desending order and return.
