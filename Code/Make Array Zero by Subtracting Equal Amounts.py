class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([x for x in nums if x]))          #In each opeeration, always uses the smallest non-zero number. So, result is the number of unique non-zero number.
