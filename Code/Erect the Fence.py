class Solution:
    def orientation(self, p: tuple, q: tuple, r: tuple) -> bool:                              #Given point p, q, r, return if r is on the right of line of p and q.
        return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0]) < 0              #Calculate the cross product of vector pq and vector qr, and return if it's smaller than 0.
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        leftBottom = (101, 101)
        for x, y in trees:                                                                    #Find the left bottom point.
            if x < leftBottom[0] or (x == leftBottom[0] and y < leftBottom[1]):
                leftBottom = (x, y)
        left, nonleft = [], []                                                                #Initialize the list of points on the leftmost vertical line(x == leftBottom[0]) and list of points not on the leftmost vertical line.
        for x, y in trees:
            if x == leftBottom[0]:                                                            #If x == leftBottom[0], append current point to left.
                left.append((x, y))
            else:                                                                             #Otherwise append current point to nonleft with addition properties to sort by.
                k = (y - leftBottom[1]) / (x - leftBottom[0])                                 #Property 1, the slope of line of leftBottom and current point, because we want to sort nonleft points by the slope.                
                d2 = (y - leftBottom[1]) ** 2 + (x - leftBottom[0]) ** 2                      #Property 2, the distance from leftBottom to current point multiply the negative of slope, because if slope is equal, we want to sort points by distance in ascending order if slope is negative and in desending order if slope is positive.
                nonleft.append((k, - k * d2, (x, y)))

        left.sort()                                                                           #Sort left.
        nonleft.sort()                                                                        #Sort nonleft.
        nonleft = [p for k, d, p in nonleft] + [left[-1]]                                     #Keep only points of nonleft and add the last point in left(has largest y), because that is the last point in traverse to close the convex hull.
        stack = [leftBottom]                                                                  #Initialize stack with leftBottom.
        for point in nonleft:                                                                 #Traverse non left, in conter-clockwise.
            while len(stack) > 1:                                                             #While len(stack) > 1, calculate if current point is on the right of the line of stack[-1] and stack[-2].
                if self.orientation(stack[-2], stack[-1], point):                             #If so, pop stack.
                    stack.pop()
                else:                                                                         #Otherwise, break loop.
                    break
            stack.append(point)                                                               #Append current point to stack.
        stack.pop()                                                                           #Pop stack, the element is left[-1]/
        stack.extend(left[1:])                                                                #Add left[1:] to stack.
        return stack                                                                          #Return stack.
