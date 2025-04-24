class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct, result, left = len(set(nums)), 0, 0          #Calculate distinct numbers count and initialize result and left of sliding window.
        count = Counter()                                      #Count each number in sliding window.
        for i, x in enumerate(nums):                           #Traverse nums to enumerate the end of subarray.
            count[x] += 1                                      #Add x to sliding window.
            while left <= i and len(count) == distinct:        #While left is not greater than i and current subarray has enough distinct numbers, move forward left.
                count[nums[left]] -= 1                         #Remove nums[left] from count.
                if not count[nums[left]]:                      #If count[nums[left]] is 0, pop nums[left] from count.
                    count.pop(nums[left])
                left += 1
            result += left                                     #All the subarrays starting before left and ending at i are complete, so add left to result.
        return result
