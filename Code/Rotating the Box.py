class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])                              #Get the dimensions.
        result = [["." for _ in range(m)] for _ in range(n)]      #Initialize result.
        for i, r in enumerate(box):                               #Traverse each row.
            count = 0                                             #Initailize count.
            for j in range(len(r) + 1):                           #Traverse current row including the end.
                if j == len(r) or r[j] == '*':                    #If reaches the end or current cell is obstacle, process rotation.
                    if j < len(r):                                #If current cell is not the end, it is obstacle, place the obstacle on corresponding cell after rotation.
                        result[j][m - 1 - i] = '*'
                    while count > 0:                              #Put the stones unrotated so far on top of current cell and reset count.
                        result[j - count][m - 1 - i] = '#'
                        count -= 1
                elif r[j] == '#':                                 #If current cell is stone, increase count.
                    count += 1
        return result
