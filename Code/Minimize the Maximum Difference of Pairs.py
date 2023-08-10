class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        @cache                                                                #Binary searcg
        def countPairs(threshold: int):                                       #Suppose nums is sorted ascendingly, count the max distinct adjacent pairs whose difference is smaller than or equal to given threshold.
            count, i = 0, 0
            while i < len(nums) - 1:                                          #Traverse nums.
                if nums[i + 1] - nums[i] <= threshold:                        #If nums[i + 1] - nums[i] <= threshold, increase count.
                    count += 1                                                #The greedy approach is guarenteed optimal.
                    i += 2                                                    #Because if not taking (i, i + 1), nums[i + 1:] should produces more pairs than nums[i:] but nums[i + 1:] is shorter so it is impossible.
                else:
                    i += 1
            return count

        if not p:                                                             #If p is 0, directly return 0.
            return 0
        nums.sort()                                                           #Sort nums.
        start, end = 0, nums[-1] - nums[0]
        while start <= end:                                                   #Binary search the min threshold and return when found.
            mid = (start + end) // 2
            if countPairs(mid) >= p and countPairs(mid - 1) < p:
                return mid
            elif countPairs(mid) < p:
                start = mid + 1
            else:
                end = mid - 1
