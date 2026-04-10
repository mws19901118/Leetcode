class Solution:
    def minimumDistance(self, nums: List[int]) -> int:                    #Same as Minimum Distance Between Three Equal Elements I.py
        indexes = defaultdict(list)
        for i, x in enumerate(nums):
            indexes[x].append(i)
        result = inf
        for index in indexes.values():
            for i in range(2, len(index)):
                result = min(result, 2 * (index[i] - index[i - 2]))
        return result if result < inf else -1
