class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[j] == nums[j - 1] + 1:                                             #While nums[j] in the range beginning at nums[i], j += 1.
                j += 1
            result.append(str(nums[i]) + "->" + str(nums[j - 1]) if j > i + 1 else str(nums[i]))            #Add range to result.
            i = j
        return result
