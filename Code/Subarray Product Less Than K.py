class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        end, product, count = 0, 1, 0                                   #Maintain a sliding window starting from start index whose product is less than k.
        for start in range(len(nums)):
            while end < len(nums) and product * nums[end] < k:          #While the product is smaller than k, extend the right end of window towards right.
                product *= nums[end]
                end += 1
            if end > start:                                             #If window size is larger than 0, add window length to count and move the number on start out of window.
                count += end - start
                product //= nums[start]
            end = max(start + 1, end)                                   #End should be at least not smaller than start.
        return count
