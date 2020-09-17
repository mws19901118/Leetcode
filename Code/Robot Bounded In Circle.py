class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        position, direction = (0, 0), (0, 1)                                                #Initialize position and direction.
        for i in range(4):                                                                  #Traverse through instructions repeatedly 4 times, if robot ends in the initial position, it will never leave the circle.
            for x in instructions:
                if x == "L":
                    direction = (-direction[1], direction[0])                               #Update direction when turn left.
                elif x == "R":
                    direction = (direction[1], -direction[0])                               #Update direction when turn right.
                else:
                    position = (position[0] + direction[0], position[1] + direction[1])     #Update position when go straight.
        return position == (0, 0) and direction == (0, 1)                                   #Return if robot ends in initial position.
