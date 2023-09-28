class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if not x & 1] + [x for x in nums if x & 1]    #Put even integers before odd integers.
