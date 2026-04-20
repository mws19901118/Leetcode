class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        result = 0
        firstIndex = {}                                                                          #Store the first index of each color.
        for i, x in enumerate(colors):                                                           #Traverse colors.
            if x not in firstIndex:                                                              #If x is not seen, store its first index.
                firstIndex[x] = i
            if len(firstIndex) > 1:                                                              #If there are at least 2 colors, find the first index which is not current color and update result if necessary.
                result = max(result, i - min(firstIndex[y] for y in firstIndex if y != x))
        return result
