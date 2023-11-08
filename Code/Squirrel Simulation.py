class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        distance, minDiff = 0, inf                                                                                                  #Initialize overall distance and min difference between distance from squirrel to nut and distance from tree to nut.
        for x, y in nuts:                                                                                                           #Traverse nuts.
            distance += abs(x - tree[0]) + abs(y - tree[1])                                                                         #Add the distance from tree to nut to overall distance.
            minDiff = min(minDiff, (abs(x - squirrel[0]) + abs(y - squirrel[1])) - (abs(x - tree[0]) + abs(y - tree[1])))           #Update the min difference between distance from squirrel to nut and distance from tree to nut.
        return 2 * distance + minDiff                                                                                               #Since all trip to nut is round trip, we double overall distance and add minDiff as we pick the it as the first nut to save the most distance.
