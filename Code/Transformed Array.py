class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + x) % len(nums)] for i, x in enumerate(nums)]        #Traverse nums; then for each index, calculate the target it lands and take the value.
