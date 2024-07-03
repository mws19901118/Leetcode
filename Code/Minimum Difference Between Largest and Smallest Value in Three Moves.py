class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:                                                                                #If nums has fewer than or equal to 4 elements, just return 0 as we can change them to same value.
            return 0
        nums.sort()                                                                                       #Sort nums.
        return min(nums[-4] - nums[0], nums[-3] - nums[1], nums[-2] - nums[2], nums[-1] - nums[3])        #Return the min difference among decresing 3 largest elements, decresing 2 largest elements and increasing the smallest element, decreasing the largest element amd increasing 2 smallest elements, increasing 3 smallest elements.
