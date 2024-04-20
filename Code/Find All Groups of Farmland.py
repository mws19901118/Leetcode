class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])                                  #Get the dimensions.
        result = []                                                     #Initialize result.
        for x, y in product(range(m), range(n)):                        #Traverse each hectare in land.
            if land[x][y] == 0:                                         #If hectare is forested land, skip.
                continue
            u = x                                                       #Find the bottom row of this farmland.
            while u < m and land[u][y] == 1:
                u += 1
            v = y                                                       #Find the right column of this farmland.
            while v < n and land[x][v] == 1:
                v += 1
            result.append([x, y, u - 1, v - 1])                         #Append the top left corner and bottom right corner to result.
            for i, j in product(range(x, u), range(y, v)):              #Change every hectare in current farm land to 2 to mark them as visited.
                land[i][j] = 2
        return result
