class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)                              #Count elements in nums.
        return all(not x & 1 for x in count.values())      #Return if all count in count.values() are even.
