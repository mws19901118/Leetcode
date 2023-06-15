class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        nums = [lower - 1] + nums + [upper + 1]                                                                   #Add lower - 1 and upper + 1 to the both end of nums respectively.
        return [[nums[i] + 1, nums[i + 1] - 1] for i in range(len(nums) - 1) if nums[i] + 1 < nums[i + 1]]        #Find all the adjacent number pairs in nums where the gap is larger than 1; convert the gap to range and return.
