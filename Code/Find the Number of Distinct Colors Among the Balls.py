class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls, count = {}, Counter()              #Store the color of each ball and the count of each color.
        result = []                               #Initialize result.
        for x, y in queries:                      #Traverse queries.
            if x in balls:                        #If x already has color, reduce the count of its color.
                count[balls[x]] -= 1
                if not count[balls[x]]:           #If the color no longer exists, pop it from count.
                    count.pop(balls[x])
            balls[x] = y                          #Set the color of ball x to y.
            count[y] += 1                         #Increase count of y.
            result.append(len(count))             #Append the length of count to result.
        return result
