class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()                                                         #Sort nums. Because we only care the length of subsequence for the entire list(not required to end at any index), the order does not matter.
        prefixSum = [0]                                                     #Calculate prefix sum of sorted nums; prefix sum of at index i is the smallest subsequence sum of length i.
        for x in nums:
            prefixSum.append(x + prefixSum[-1])
        return [bisect.bisect_right(prefixSum, x) - 1 for x in queries]     #Binary search for the rightmost index to insert each query then minus 1. If query is greater than or equal to a prefix sum at index i, it could contain the subsequence with length i.
