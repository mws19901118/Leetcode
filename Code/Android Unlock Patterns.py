class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        forbidden = set([(1, 3), (4, 6), (7, 9), (1, 7), (2, 8), (3, 9), (1, 9), (3, 7)])                                                          #Store the potential forbidden segments.
        bitMasks = {i: 1 << (i - 1) for i in range(1, 10)}                                                                                         #Initialize bit masks for each dot.
        @cache                                                                                                                                     #Cache result.
        def backtracking(state: int, lastDot: int, left: int) -> int:                                                                              #Backtracking with current visited dots, last dot and left dot to visited.
            if not left:                                                                                                                           #If no more left dots, return 1.
                return 1
            count = 0
            for i in range(1, 10):                                                                                                                 #Traverse 1 to 9.
                if state & bitMasks[i]:                                                                                                            #If current dot is visited, skip.
                    continue
                if lastDot and ((i, lastDot) in forbidden or (lastDot, i) in forbidden) and not (state & bitMasks[(i + lastDot) // 2]):            #If there is a last dot and the segment of last dot and current dot is in forbidden set and the middle dot of segment is not visited, skip current dot as no jump through allowed.
                    continue
                count += backtracking(state | bitMasks[i], i, left - 1)                                                                            #Add the result from next backtrack to count.
            return count                                                                                                                           #Return count.

        return sum(backtracking(0, 0, x) for x in range(m, n + 1))                                                                                 #Traverse m to n and sum up the result of backtracking(0, 0, x).
