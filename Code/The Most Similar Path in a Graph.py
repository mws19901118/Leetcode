class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        dp = [[len(targetPath) + 1] * n for _ in range(len(targetPath))]                #Initialize the dp matrix, dp[i][j] means the min edit distance between targetPath[:i + 1] and any path with same length that ends at city j.
        path = [[-1] * n for _ in range(len(targetPath))]                               #Initialize the previous city in path with the min edit distance at dp[i][j].
        for i in range(n):                                                              #For i == 0, the edit distance is if names[i] is not same as targetPath[0].
            dp[0][i] = int(names[i] != targetPath[0])
        for i in range(1, len(targetPath)):                                             #Iterate for 1 to len(targetPath) - 1.
            for x, y in roads:                                                          #Traverse all city pairs connected directly by road; dp[i + 1][j] = min(dp[i][k]) + editDistance(targetPath[i + 1], names[j]), k is in the neighbors of j.
                if dp[i - 1][x] < dp[i][y]:                                             #Update dp[i][y] and path[i][y] if dp[i - 1][x] is smaller.
                    dp[i][y] = dp[i - 1][x]
                    path[i][y] = x
                if dp[i - 1][y] < dp[i][x]:                                             #Update dp[i][x] and path[i][x] if dp[i - 1][y] is smaller.
                    dp[i][x] = dp[i - 1][y]
                    path[i][x] = y
            for j in range(n):                                                          #For each city, add the edit distance between targetPath[i + 1] and names[j] to dp[i][j]
                dp[i][j] += int(names[j] != targetPath[i])
        minDistance = min(dp[-1])                                                       #Find the min edit distance for the entire target path.
        result = [dp[-1].index(minDistance)]                                            #Also find the cities at which the min edit distance path ends.
        for i in range(len(targetPath) - 1):                                            #Traverse back to find the whole path.
            result.append(path[-(i + 1)][result[-1]])
        return reversed(result)                                                         #Reverse result and return.
      
