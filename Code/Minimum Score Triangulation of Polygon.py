class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache                                                                                              #Cache result.
        def dp(x: int, y: int) -> int:                                                                      #Calculate the min score in values[x:y + 1].
            if x + 2 > y:                                                                                   #If there are fewer than 3 vertices, return 0.
                return 0
            if x + 2 == y:                                                                                  #If there are exactly 3 vertices, return the product of their values.
                return values[x] * values[x + 1] * values[x + 2]
            return min(values[x] * values[y] * values[i] + dp(x, i) + dp(i, y) for i in range(x + 1, y))    #Enumerate the vertex in values[x + 1:y], put x, y, i in a triangle then recursively calculate dp(x, i) and dp(i, y) to get the current triangulation score. Then return the min score.
        return dp(0, len(values) - 1)                                                                       #Return dp(0, len(values) - 1).
