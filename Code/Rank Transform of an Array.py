class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        indexes = defaultdict(list)              #Store the indexes for each value.
        for i, x in enumerate(arr):
            indexes[x].append(i)
        sortedValue = sorted(indexes.keys())     #Sort distinct values.
        result = [0] * len(arr)
        for i, x in enumerate(sortedValue):      #Traverse distinct values.
            for index in indexes[x]:             #Traverse the indexes of each value.
                result[index] = i + 1            #Set the rank for each index.
        return result
