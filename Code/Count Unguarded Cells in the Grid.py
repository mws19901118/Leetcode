class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows, cols = [[(-1, 'W'), (n, 'W')] for _ in range(m)], [[(-1, 'W'), (m, 'W')] for _ in range(n)]    #Initialize each row and column, with walls on both end.
        unguarded = set((i, j) for i, j in product(range(m), range(n)))                                      #Initialize the set of unguarded cells to be entire matrix.
        for x, y in guards:                                                                                  #Traverse guards.
            rows[x].append((y, 'G'))                                                                         #Add y coordinate and label 'G' to rows[x].
            cols[y].append((x, 'G'))                                                                         #Add x coordinate and label 'G' to cols[y].
            unguarded.remove((x, y))                                                                         #Remove current cell from unguarded.
        for x, y in walls:                                                                                   #Traverse walls.
            rows[x].append((y, 'W'))                                                                         #Add y coordinate and label 'W' to rows[x].
            cols[y].append((x, 'W'))                                                                         #Add x coordinate and label 'W' to cols[y].
            unguarded.remove((x, y))                                                                         #Remove current cell from unguarded.
        for i, r in enumerate(rows):                                                                         #Traverse rows.
            r.sort()                                                                                         #Sort current row.
            for j in range(len(r) - 1):                                                                      #Traverse each adjacent pairs in current row.
                if r[j][1] == 'G' or r[j + 1][1] == 'G':                                                     #If either label of the pair is 'G', remove all cells in between from unguarded.
                    for k in range(r[j][0] + 1, r[j + 1][0]):
                        unguarded.discard((i, k))
        for i, c in enumerate(cols):                                                                         #Traverse cols.
            c.sort()                                                                                         #Sort current column.
            for j in range(len(c) - 1):                                                                      #Traverse each adjacent pairs in current column.
                if c[j][1] == 'G' or c[j + 1][1] == 'G':                                                     #If either label of the pair is 'G', remove all cells in between from unguarded.
                    for k in range(c[j][0] + 1, c[j + 1][0]):
                        unguarded.discard((k, i))
        return len(unguarded)uar]                                                                            #Return the length of unguarded.
