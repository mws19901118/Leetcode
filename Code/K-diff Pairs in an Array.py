class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count, pairs = Counter(nums), 0                                             #Count nums.
        for x in count:                                                             #Iterate over each value.
            pairs += (k > 0 and x + k in count) or (k == 0 and count[x] > 1)        #If k > 0 and x + k in count or k == 0 and count[x] > 1, there is a pair.
        return pairs
