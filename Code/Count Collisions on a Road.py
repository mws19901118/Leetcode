class Solution:
    def countCollisions(self, directions: str) -> int:
        count, result, hasS = 0, 0, False      #Initialize moving right car count, result and if there is staionary car to the left.
        for x in directions:                   #Traverse directions.
            if x == 'R':                       #If current car is moving right, increase count.
                count += 1
            elif x == 'L':                     #If current car is moving left, check potential collision.
                if count:                      #If there are cars moving right, all the cars will be colliding with current car, so add count + 1 to result.
                    result += count + 1
                    count = 0                  #Reset count.
                    hasS = True                #Set c
                elif hasS:                     #Otherwise if there is stationary car, it will collide with current car so increase result by 1.
                    result += 1
            else:                              #If current car is stationary, check potential collision.
                if count:                      #Just like processing 'L' but doesn't count current car in collision.
                    result += count
                    count = 0
                hasS = True                    #Set has statinary car to true.
        return result
