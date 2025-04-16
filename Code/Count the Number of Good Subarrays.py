class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pairs, start, result = 0, 0, 0              #Initialize pairs count, start of sliding window and result.
        count = Counter()                           #Count each number in sliding window.
        for i, x in enumerate(nums):                #Traverse nums to enumerate the end of subarray.
            pairs += count[x]                       #Add x to sliding window, which should create count[x] new pairs.
            count[x] += 1                           #Update count x.
            while start <= i and pairs >= k:        #While start is not greater than i and there are at least k pairs, move forward start. 
                count[nums[start]] -= 1             #Update count[nums[start]].
                pairs -= count[nums[start]]         #Remove count[nums[start]] pairs.
                start += 1                          #Increase start.
            result += start                         #Only subarrays starting from 0 to start - 1 will have enough pairs
        return result
