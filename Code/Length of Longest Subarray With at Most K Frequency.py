class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = Counter()                              #Count each element.
        start, result = 0, 0                           #Initialize the start of sliding window and result.
        for i, x in enumerate(nums):                   #Traverse nums to enumerate the end of sliding window.
            count[x] += 1                              #Increase the count of current element.
            while count[x] > k and start < i:          #While count[x] is greater than k and start < i(sliding window has at least one element), move forward start.
                count[nums[start]] -= 1                #Decrease the count of element on start.
                start += 1
            result = max(result, i - start + 1)        #Update result if current window size is greater.
        return result
