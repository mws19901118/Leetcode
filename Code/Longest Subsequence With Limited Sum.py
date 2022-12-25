class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()                                                         #Sort nums. Because we only care the length of subsequence for the entire list(not required to end at any index), the order does not matter.
        prefixSum = [0]                                                     #Initialize prefix sum of sorted nums.
        for x in nums:
            prefixSum.append(x + prefixSum[-1])
        return [bisect.bisect_right(prefixSum, x) - 1 for x in queries]     #Binary search for the rightmost index to insert each query then minus 1. If query is greater than or equal to a prefix sum, it could take the subsequence with length equals to the index.
