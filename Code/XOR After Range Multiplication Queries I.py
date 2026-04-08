class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        division = 10 ** 9 + 7                        #Initialize division.
        for l, r, k, v in queries:                    #Traverse queries.
            for i in range(l, r + 1, k):              #Traverse each element of this query and apply opeartion.
                nums[i] = (nums[i] * v) % division
        return reduce(lambda x, y: x ^ y, nums)       #Return the overall XOR result.
