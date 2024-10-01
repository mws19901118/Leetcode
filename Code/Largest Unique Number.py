class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)                                  #Count each number.
        candidates = [x for x in count if count[x] == 1]       #Filter out candidates whose count is 1.
        return -1 if not candidates else max(candidates)       #Return -1 if no such candidates; otherwise return the max of candidates.
