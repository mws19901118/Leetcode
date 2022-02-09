class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)                                                                   #Count nums.
        return sum((k > 0 and x + k in count) or (k == 0 and count[x] > 1) for x in count)      #If k > 0 and x + k in count or k == 0 and count[x] > 1, there is a pair.
