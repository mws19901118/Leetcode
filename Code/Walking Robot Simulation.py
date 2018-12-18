class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        xMap = dict()                                                                           #Hash obstacles y coordinate by x coordinate.
        yMap = dict()                                                                           #Hash obstacles x coordinate by y coordinate.
        for o in obstacles:
            if o[0] not in xMap:
                xMap[o[0]] = []
            xMap[o[0]].append(o[1])
            if o[1] not in yMap:
                yMap[o[1]] = []
            yMap[o[1]].append(o[0])
                
        for x in xMap:                                                                          #Sort y coordinate for each obstacle x.
            xMap[x].sort()
        for y in yMap:                                                                          #Sort x coordinate for each obstacle y.
            yMap[y].sort()
        
        leftTurnMap = {}                                                                        #Hash the direction after left turn by the direction before left turn.
        leftTurnMap[(0, 1)] = (-1, 0)
        leftTurnMap[(-1, 0)] = (0, -1)
        leftTurnMap[(0, -1)] = (1, 0)
        leftTurnMap[(1, 0)] = (0, 1)
        
        rightTurnMap = {}                                                                       #Hash the direction after right turn by the direction before right turn.
        rightTurnMap[(0, 1)] = (1, 0)
        rightTurnMap[(1, 0)] = (0, -1)
        rightTurnMap[(0, -1)] = (-1, 0)
        rightTurnMap[(-1, 0)] = (0, 1)
        
        maxDist = 0
        point = (0, 0)
        direction = (0, 1)
        for c in commands:
            if c == -1:                                                                         #Turn right.
                direction = rightTurnMap[direction]
            elif c == -2:                                                                       #Turn left.
                direction = leftTurnMap[direction]
            else:                                                                               #Move forward.
                point = self.move(point, direction, c, xMap, yMap)
            maxDist = max(pow(point[0], 2) + pow(point[1], 2), maxDist)
        return maxDist
    
    def move(self, point, direction, distance, xMap, yMap):
        nextPoint = (point[0] + direction[0] * distance, point[1] + direction[1] * distance)
        obstacle = None
        if direction == (0, 1):                                                                 #Go up.
            obstacle = self.find(point, distance, direction, xMap)
        elif direction == (1, 0):                                                               #Go right.
            obstacle = self.find(point, distance, direction, yMap)
        elif direction == (0, -1):                                                              #Go down.
            obstacle = self.find(point, distance, direction, xMap)
        else:                                                                                   #Go left.
            obstacle = self.find(point, distance, direction, yMap)
        
        if obstacle:                                                                            #If encounters obstacle, stop 1 grid before the obstacle.
            nextPoint = (obstacle[0] - direction[0], obstacle[1] - direction[1])
        return nextPoint
    
    def find(self, point, distance, direction, obstacleMap):                                    #Find the obstacle given current point, distance, direction and obstacle hashmap.
        obstacle = None
        factor = direction[0] + direction[1]                                                    #Factor indicates if the robot is going on positive direction on either X or Y.
        unchangedCoordinate = point[0]                                                          #Based on the direction is on X or Y, find the coordinate would be changed and coordinate would not be changed for currect move.
        changedCoordinate = point[1]
        if direction[0]:
            unchangedCoordinate = point[1]
            changedCoordinate = point[0]
        if unchangedCoordinate not in obstacleMap:                                              #If there is no obstacles on current direction, return None.
            return obstacle
        obstaclesWithGivenCoordinate = obstacleMap[unchangedCoordinate]                         #Otherwise, get the sorted obstacle coordinates.
        target = changedCoordinate + distance * factor                                          #Calculate the target for changed coordinate.
        start = 0
        end = len(obstaclesWithGivenCoordinate) - 1
        obstacleCoordinate = None
        while start <= end:                                                                     #Begin binary search. Based on the execution on dataset on Leetcode, it does not have a significant improvement than linear search.
            mid = int((start + end) / 2) 
            if obstaclesWithGivenCoordinate[mid] * factor > target * factor:                    #If mid of obstacle coordinates in beyond target: go to the 2nd half(if positive direction) or 1st half(if negative direction) of obstacle coordinates to find a closer obstacle.
                if factor == 1:
                    end = mid - 1
                else:
                    start = mid + 1
            elif obstaclesWithGivenCoordinate[mid] * factor <= changedCoordinate * factor:      #If mid of obstacle coordinates is behind current coordinate: go to the 1st half(if positive direction) or 2nd half(if negative direction) of obstacle to find a possible obstacle.
                if factor == 1:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                obstacleCoordinate = obstaclesWithGivenCoordinate[mid]                          #If the mid of obstacle coordinates can block the move, store it in obstacleCoordinate and find a closer obstacle.
                if factor == 1:
                    end = mid - 1
                else:
                    start = mid + 1
        if obstacleCoordinate is not None:                                                      #If obstacle found, group the coordinate with unchanged coordinate to return the coordinates of obstacle.
            if direction[0]:
                obstacle = (obstacleCoordinate, unchangedCoordinate)                
            else:
                obstacle = (unchangedCoordinate, obstacleCoordinate)
        return obstacle
