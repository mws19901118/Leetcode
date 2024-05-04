class Solution:                                                                        #Return count. 
    def largestIsland(self, grid: List[List[int]]) -> int:
        def BFS(self, grid: List[List[int]], i: int, j: int, label: int) -> int:                      #Label island and calculate area using BFS.
            count = 0                                                                                 #Initialize area.
            grid[i][j] = label                                                                        #Label current cell.
            q = [(i, j)]                                                                              #Initialize queue.
            while q:                                                                                  #BFS.
                newq = []                                                                             #Initialize new queue.
                count += len(q)                                                                       #Add the length of current queue to count.
                for x, y in q:                                                                        #Traverse queue.
                    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:                   #Traverse neighbors of current cell.
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid) and grid[nx][ny] == 1:         #If it's valid and is 1, label it and append it to newq.
                            grid[nx][ny] = label
                            newq.append((nx, ny))
                q = newq                                                                              #Replace q with newq.
            return count
            
        result, label = 0, 2                                                                          #Initialize result and island label at 2.
        areaByLabel = {}                                                                              #Use a dict to store the island area by label.
        for i, j in product(range(len(grid)), range(len(grid))):                                      #Traverse grid.
            if grid[i][j] == 1:                                                                       #If current cell is 1, label its entire island using BFS and get the area.
                areaByLabel[label] = BFS(i, j, label)
                result = max(result, areaByLabel[label])                                              #Update result to be the max island area.
                label += 1                                                                            #Increase label.
        for i, j in product(range(len(grid)), range(len(grid))):                                      #Traverse grid.
            if grid[i][j] == 0:                                                                       #If current cell is 0, use a set to store the labels of adjacent islands.
                labels = set()
                for x, y in [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]:
                    if 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] != 0:
                        labels.add(grid[x][y])
                result = max(result, sum(areaByLabel[l] for l in labels) + 1)                         #Sum up the areas of adjacent islands then plus 1 and update result if necessary.
        return result
