class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        @cache                                                                                          #Cache result.
        def countMissing(index: int) -> int:                                                            #Count missing elements before nums[index].
            return nums[index] - nums[0] - index                                                        #Since nums is strictly increasing, there are index elements in the range from nums[0] to nums[index], so count of missing elements is nums[index] - nums[0] - index.

        start, end = 0, len(nums) - 1
        while start <= end:                                                                             #Binary search in nums.
            mid = (start + end) // 2
            if countMissing(mid) < k and (mid == len(nums) - 1 or countMissing(mid + 1) >= k):          #If missing elements count before nums[mid] is smaller than k and either mid is the end of nums or missing elements count before nums[mid + 1] is greater than k, the last index before k-th missing element is mid.
                return nums[mid] + k - countMissing(mid)                                                #So, add the gap between missing elements count before nums[mid] to k to nums[mid], then return.
            elif countMissing(mid) >= k:                                                                #If missing elements count before nums[mid] is greater than or equal to k, k-th missing element is before nums[mid], so keep binary search in the first half.
                end = mid - 1
            else:                                                                                       #Otherwise, k-th missing element is after nums[mid + 1], so keep binary search in the second half.
                start = mid + 1
