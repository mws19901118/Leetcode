class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        minesSet = set([(x, y) for x, y in mines])                                                                                                                                                                  #Put all coordinates of mines in a set.
        left, right, top, bottom = [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)], [[0 for _ in range(n)] for _ in range(n)]       #Initialize count of 1(including self) on each side of current coordinate.
        for i, j in product(range(n), range(n)):                                                                                                                                                                    #Traverse grid forward.
            if (i, j) in minesSet:                                                                                                                                                                                  #If current coordinate is a mine, continue.
                continue
            left[i][j] = 1 if j - 1 < 0 or (i, j - 1) in minesSet else left[i][j - 1] + 1                                                                                                                           #Update left[i][j].
            top[i][j] = 1 if i - 1 < 0 or (i - 1, j) in minesSet else top[i - 1][j] + 1                                                                                                                             #Update top[i][j].
        for i, j in product(reversed(range(n)), reversed(range(n))):                                                                                                                                                #Traverse grid backward.
            if (i, j) in minesSet:
                continue
            right[i][j] = 1 if j + 1 >= n or (i, j + 1) in minesSet else right[i][j + 1] + 1                                                                                                                        #Update right[i][j].
            bottom[i][j] = 1 if i + 1 >= n or (i + 1, j) in minesSet else bottom[i + 1][j] + 1                                                                                                                      #Update bottom[i][j].
        return max(min(left[i][j], top[i][j], right[i][j], bottom[i][j]) for i, j in product(range(n), range(n)))                                                                                                   #Return the max value of min(left[i][j], top[i][j], right[i][j], bottom[i][j]) for any i, j.
