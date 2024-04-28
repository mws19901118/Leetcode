class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        letterIndexes = defaultdict(list)                                                                                                                            #Store the indexes in ring for each letter.
        for i, x in enumerate(ring):
            letterIndexes[x].append(i)
        leftIndex, rightIndex = [defaultdict(int) for _ in range(len(ring))], [defaultdict(int) for _ in range(len(ring))]                                           #For each index, store the first index on its left for each letter. Also store the same for right.
        for i, x in enumerate(ring):                                                                                                                                 #Traverse ring.
            for y in letterIndexes:                                                                                                                                  #Traverse all distinct letters.
                if x == y:                                                                                                                                           #If x is same with y, leftIndex[i][y] and right[i][y] is just current index. This likely not making any difference, since we should never ends up at one letter in the middle of a few consecutive same letters.
                    leftIndex[i][y] = i
                    rightIndex[i][y] = i
                    continue
                leftIndex[i][y] = letterIndexes[y][-1] if i < letterIndexes[y][0] else letterIndexes[y][bisect_right(letterIndexes[y], i) - 1]                       #If i < letterIndexes[y][0], leftIndex[i][y] = letterIndexes[y][-1] as we it is a cycle; otherwise, binary search for last index of y that is smaller than i.
                rightIndex[i][y] = letterIndexes[y][0] if i > letterIndexes[y][-1] else letterIndexes[y][bisect_left(letterIndexes[y], i)]                           #If i > letterIndexes[y][-1], leftIndex[i][y] = letterIndexes[y][0] as we it is a cycle; otherwise, binary search for first index of y that is greater than i.

        @cache                                                                                                                                                       #Cache result.
        def dp(indexInKey: int, indexInRing: int) -> int:                                                                                                            #DP for the minimal number of steps for key[indexInKey:] with the current index of ring that is on 12:00.
            if indexInKey == len(key):                                                                                                                               #If indexInKey reaches the end, return 0.
                return 0
            curr = key[indexInKey]                                                                                                                                   #Get the current letter to spell.
            indexLeft = leftIndex[indexInRing][curr]                                                                                                                 #Look up the first idnex of curr on left of indexInRing.
            leftDistance = (indexInRing - indexLeft) if indexInRing >= indexLeft else (indexInRing - indexLeft + len(ring))                                          #Calculate distance to turn left to leftIndex.
            indexRight = rightIndex[indexInRing][curr]                                                                                                               #Look up the first idnex of curr on right of indexInRing.
            rightDistance = (indexRight - indexInRing) if indexInRing <= indexRight else (indexRight - indexInRing + len(ring))                                      #Calculate distance to turn right to rightIndex.
            return min(dp(indexInKey + 1, indexLeft) + leftDistance, dp(indexInKey + 1, indexRight) + rightDistance) + 1                                             #Result is the smaller of leftDistance + dp(indexInKey + 1, indexLeft) and rightDistance + dp(indexInKey + 1, indexRight) then plus 1.

        return dp(0, 0)                                                                                                                                              #Return the result of dp(0, 0).
