class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p, start, count = 1, 0, 0                                        #Maintain a sliding window starting from start index whose product is less than k.
        for i, x in enumerate(nums):                                     #Traverse nums.
            p *= x                                                       #Multiply x to product.
            while p >= k and start <= i:                                 #While product is greater than or equal to k and start is not greater than i, move forward the start of window.
                p //= nums[start]                                        #Also update product.
                start += 1
            count += i - start + 1                                       #Add the window size(i - start + 1) to count.
        return count
