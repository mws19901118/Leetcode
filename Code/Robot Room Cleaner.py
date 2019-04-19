# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        leftTurn = {(0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1)}   #Initialize the map of directions for left turn.
        rightTurn = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}  #Initialize the map of directions for right turn.

        x, y = 0, 0                                                                       #Initialize the relative coordinate from inital cell.
        direction = (0, 1)                                                                #Initialize the direction, facing up.
        stack = [0]                                                                       #Use a stack to store how many directions have been traversed for current cell.
        trace = set([(0, 0)])                                                             #Use a set to store all relative coordinates of cleaned cells.
        robot.clean()                                                                     #Clean initial position.
        while stack:                                                                      #While stack is not empty, do DFS.
            if (len(stack) == 1 and stack[-1] < 4) or stack[-1] < 3:                      #If the length of stack is 1 and the top of stack is smaller than 4(we need to traverse 4 directions for initial cell) or top of stack is smaller than 3, we still have directions to traverse for current cell.
                if (x + direction[0], y + direction[1]) not in trace and robot.move():    #If the target cell after move is not cleaned and is not blocked cell, move to target cell.
                    x += direction[0]                                                     #Update relative coordinate.
                    y += direction[1]
                    robot.clean()                                                         #Clean current cell.
                    robot.turnLeft()                                                      #Turn left so we start traverse with directions in the order of left, straight and right.
                    direction = leftTurn[direction]
                    stack.append(0)                                                       #Append 0 to stack.
                    trace.add((x, y))                                                     #Add relative coordinate to trace.
                else:                                                                     #Otherwise, turn tight to next direction.
                    robot.turnRight()
                    direction = rightTurn[direction]
                    stack[-1] += 1                                                        #Plus 1 to the stack top since we have finished traversing towards one direction.
            else:                                                                         #If we have traversed all directions.
                robot.move()                                                              #Move back robot.
                x += direction[0]                                                         #Update relative coordinate.
                y += direction[1]
                robot.turnLeft()                                                          #Turn around robot.
                direction = leftTurn[direction]
                robot.turnLeft()
                direction = leftTurn[direction]
                stack.pop()                                                               #Pop stack.
