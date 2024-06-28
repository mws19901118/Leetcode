class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n                                                           #Count the roads each city has.
        for a, b in roads:
            count[a] += 1
            count[b] += 1
        return sum(x * (i + 1) for i, x in enumerate(sorted(count)))              #Sort count and assign cities who has more roads higher importance. Then calculate the total importance.
