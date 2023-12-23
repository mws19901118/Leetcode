class Solution:
    def isPathCrossing(self, path: str) -> bool:
        moves = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}      #Initialize moves.
        x, y = 0, 0                                                         #Initialize where the unit is.
        visited = set([(x, y)])                                             #Store visited locations.
        for p in path:                                                      #Traverse path.
            x += moves[p][0]                                                #Move unit.
            y += moves[p][1]
            if (x, y) in visited:                                           #If current location is already visited, return true.
                return True
            visited.add((x, y))                                             #Add current location to visited.
        return False                                                        #Return false if not crossing.
