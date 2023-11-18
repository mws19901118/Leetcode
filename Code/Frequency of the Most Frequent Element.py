class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()                                                                                        #Sort nums. The most frequent number must be an existing number. Because if not, suppose it is between nums[i] and nums[i + 1], then nums[i] is also max frequent with fewer operations needed.
        left, right, count, result = 0, 0, 0, 0                                                            #Initialize the left and right boundary of a sliding window. Also initialize the count of operation used and result.
        while right < len(nums):                                                                           #Traverse while the right boundary not reaching the end of nums yet.
            count += (right - left) * (nums[right] - (nums[right - 1] if right >= 1 else 0))               #Update count to increase all numbers in window to nums[right].
            while left <= right and count > k:                                                             #While left boundary is not exceeding right boundary and count is greater than k, move left out of bound.
                count -= nums[right] - nums[left]                                                          #Update count.
                left += 1                                                                                  #Move left to next.
            result = max(result, right - left + 1)                                                         #Update result if necessary.
            right += 1                                                                                     #Move right to next.
        return result
