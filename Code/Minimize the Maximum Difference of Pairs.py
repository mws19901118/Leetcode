class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        @cache                                                                #Cache result.
        def countPairs(threshold: int) -> bool:                               #Suppose nums is sorted ascendingly, count the max distinct adjacent pairs whose difference is smaller than or equal to given threshold.
            if threshold < 0:
                return False
            count, i = 0, 0
            while i < len(nums) - 1:                                          #Traverse nums.
                if nums[i + 1] - nums[i] <= threshold:                        #If nums[i + 1] - nums[i] <= threshold, increase count.
                    count += 1                                                #The greedy approach is guarenteed optimal.
                    i += 2                                                    #Because if not taking (i, i + 1), nums[i + 1:] should produces more pairs than nums[i:] but nums[i + 1:] is shorter so it is impossible.
                else:
                    i += 1
            return count >= p

        nums.sort()                                                           #Sort nums.
        start, end = 0, nums[-1] - nums[0]
        while start <= end:                                                   #Binary search the min threshold and return when found.
            mid = (start + end) // 2
            if countPairs(mid) and not countPairs(mid - 1):
                return mid
            elif not countPairs(mid):
                start = mid + 1
            else:
                end = mid - 1
