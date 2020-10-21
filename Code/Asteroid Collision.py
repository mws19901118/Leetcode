class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []                                      #Use stack to store asteroids after collision.
        for x in asteroids:
            while x < 0 and stack and stack[-1] > 0:    #While current asteriod is smaller than 0 and stack is not empty and top of stack is greater than 0.
                if stack[-1] < -x:                      #If current asteriod is bigger, pop stack and continue.
                    stack.pop()
                    continue
                elif stack[-1] == -x:                   #If they have same size, pop stack and break.
                    stack.pop()
                break                                   #Otherwise just break.
            else:                                       #If not go in to while loop, append current asteriod to stack cause there won't be collision.
                stack.append(x)
        return stack
