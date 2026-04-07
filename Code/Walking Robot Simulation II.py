class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height                                                              #Store width and height.
        self.x, self.y, self.u, self.v = 0, 0, 1, 0                                                          #Initialize position and direction.
        self.leftTurn = {(-1, 0): (0, -1), (0, 1): (-1, 0), (1, 0): (0, 1), (0, -1): (1, 0)}                 #Map the direction after left turn to current direction.
        self.directions = {(-1, 0): "West", (0, 1): "North", (1, 0): "East", (0, -1): "South"}               #Store the direction names.

    def distanceToEdge(self) -> int:                                                                         #Calculate the distance to first edge.
        if self.getDir() == "West":
            return self.x
        elif self.getDir() == "North":
            return self.height - 1 - self.y
        elif self.getDir() == "East":
            return self.width - 1 - self.x
        else:
            return self.y

    def shorten(self, num: int) -> int:                                                                     #Shorten the number of steps.
        distance = 0                                                                                        #Calculate the distance to first corner.
        if self.getDir() == "West":
            distance = self.x + self.y
        elif self.getDir() == "North":
            distance =  self.height - 1 - self.y + self.x
        elif self.getDir() == "East":
            distance =  self.width - 1 - self.x + self.height - 1 - self.y
        else:
            distance =  self.y + self.width - 1 - self.x
        return distance + (num - distance) % ((self.width - 1 + self.height - 1) * 2)                       #After arriving first corner, the robot just walks along edges in counterclockwise loop after loop, so we only need the last part.

    def step(self, num: int) -> None:
        num = self.shorten(num)                                                                             #Shorten num first.
        while True:                                                                                         #Iterate.
            distance = min(num, self.distanceToEdge())                                                      #The distsance to travel is the min value of num and distance to edge.
            self.x += self.u * distance                                                                     #Move robot.
            self.y += self.v * distance
            num -= distance                                                                                 #Deduct distance from num.
            if not num:                                                                                     #If num is 0, stop.
                break
            else:                                                                                           #Otherwise, take a left turn.
                self.u, self.v = self.leftTurn[(self.u, self.v)]

    def getPos(self) -> List[int]:                                                                          #Return position.
        return [self.x, self.y]

    def getDir(self) -> str:                                                                                #Return direction.
        return self.directions[(self.u, self.v)]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
