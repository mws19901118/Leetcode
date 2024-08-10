class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)                                                                                                                                                                                      #Get the dimensions.
        adjacent = {"total": [(-1, 0), (0, 1), (1, 0), (0, -1)], "upleft": [(-1, 0), (0, -1)], "downright": [(1, 0), (0, 1)], "upright": [(-1, 0), (0, 1)], "downleft": [(1, 0), (0, -1)]}                 #For each type of region, store the available directions to traverse from the region.
        possibleTags = {(-1, 0): ["total", "downleft", "downright"], (0, -1): ["total", "upright", "downright"], (1, 0): ["total", "upleft", "upright"], (0, 1): ["total", "upleft", "downleft"]}          #For each type of direction, store the type of region it can reach.
        nodes = set()                                                                                                                                                                                      #Store all nodes in a set.
        for i, j in product(range(n), range(n)):                                                                                                                                                           #Traverse grid.
            if grid[i][j] == ' ':                                                                                                                                                                          #If current cell is ' ', add its coordinate with tag 'total' to nodes.
                nodes.add((i, j, "total"))
            elif grid[i][j]  == '/':                                                                                                                                                                       #If current cell is '/', add its corrdinate with tag 'upleft' and its coordinate with tag 'downright' to nodes.
                nodes.add((i, j, "upleft"))
                nodes.add((i, j, "downright"))
            else:                                                                                                                                                                                          #If current cell is '\', add its corrdinate with tag 'upright' and its coordinate with tag 'downleft' to nodes.
                nodes.add((i, j, "upright"))
                nodes.add((i, j, "downleft"))
        result = 0
        while nodes:                                                                                                                                                                                       #Iterate while nodes is not empty.
            q = [list(nodes)[0]]                                                                                                                                                                           #Get one node.
            nodes.remove(q[0])                                                                                                                                                                             #Remove it from nodes.
            while q:                                                                                                                                                                                       #BFS.
                newq = []
                for x, y, tag in q:                                                                                                                                                                        #Traverse nodes in q.
                    for u, v in adjacent[tag]:                                                                                                                                                             #Traverse possible directions.
                        i, j = x + u, y + v                                                                                                                                                                #Update coordinates.
                        for p in possibleTags[(u, v)]:                                                                                                                                                     #Traverse possible tags.
                            if (i, j, p) in nodes:                                                                                                                                                         #If the neighbor nodes is available, append it to newq and remove it from nodes.
                                newq.append((i, j, p))
                                nodes.remove((i, j, p))
                q = newq                                                                                                                                                                                   #Replace q with newq.
            result += 1                                                                                                                                                                                    #Increase result.
        return result
