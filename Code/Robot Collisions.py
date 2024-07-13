class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted((p, h, d) for p, h, d in zip(positions, healths, directions))      #Sort robots by position in asending order.
        indexes = {x:i for i, x in enumerate(positions)}                                   #Contruct the mapping of robot position to its index.
        result, stack = [], []                                                             #Initialize result and a stack to track all robots moving right that still survive currently.
        for p, h, d in robots:                                                             #Traverse robots.
            if d == 'R':                                                                   #If direction is right, append position and health to result.
                stack.append([p, h])
            else:
                while stack and stack[-1][1] < h:                                          #Pop stack while it is not empty and the top of stack has lower health.
                    stack.pop()
                    h -= 1                                                                 #Reduce h by 1 after collision.
                if stack and stack[-1][1] == h:                                            #If stack is not empty and the top of stack has same health, pop stack.
                    stack.pop()
                elif stack and stack[-1][1] > h:                                           #If stack is not empty and the top of stack has greater health, decrease the health by 1.
                    stack[-1][1] -= 1
                else:                                                                      #Otherwise there is no stack, current robot will survive, append original position and current health to result.
                    result.append([p, h])
        result.extend(stack)                                                               #All remaining robots in stack will survive eventaully, extend result with stack.
        return [h for p, h in sorted(result, key = lambda x: indexes[x[0]])]               #Sort result by the order of its index, and only return current health.
