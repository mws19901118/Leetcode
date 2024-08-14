class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        @cache                                                                  #Cache result.
        def countPair(threshold: int) -> int:                                   #Cound pairs smaller than or equal to threshold.
            right, count = 0, 0                                                 #Initialize the right pointer of sliding window and count.
            for i, x in enumerate(nums):                                        #Traverse nums.
                while right < len(nums) and nums[right] <= x + threshold:       #While right is not reaching the end and nums[right] <= x + threshold, move forward right.
                    right += 1
                count += right - i - 1                                          #All the pair which starts at i and ends in nums[i + 1:right] is a pair that is smaller than or equal to threshold.
            return count                                                        #Return count.

        nums.sort()                                                             #Sort nums.
        start, end = 0, nums[-1] - nums[0]                                      #Initialize start and end.
        while start <= end:                                                     #Binary search.
            mid = (start + end) // 2                                            #Calculate mid.
            if countPair(mid) >= k and countPair(mid - 1) < k:                  #If there are at least k pairs that are not greater than mid and fewer than k pairs that are not greater than mid - 1, mid is the k-th smallest pair.
                return mid
            elif countPair(mid - 1) >= k:                                       #If there are at least k pairs that are not greater than mid - 1, move end to mid - 1.
                end = mid - 1
            else:                                                               #Otherwise, move start to mid + 1.
                start = mid + 1
