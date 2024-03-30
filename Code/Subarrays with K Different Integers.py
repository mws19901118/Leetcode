class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = Counter()                     #Use a counter to count the appearance of number in sliding window.
        result, length, j = 0, 0, 0           #For each index i, length represents the distance between the first j and last j that nums[j]...nums[i] is a subarray with k different integers. Also initialize j.
        for i in range(len(nums)):
            count[nums[i]] += 1               #For each index i, add 1 to the count of nums[i].
            if len(count) < k:                #If count has less than k entries, subarray nums[j]...nums[i] does not have k different integers yet, so continue.
                continue
            elif len(count) == k:             #If count has k entries, subarray nums[j]...nums[i] has k different integers for the first time or is extending a such subarray.
                length = max(length, 1)       #So, length should be the max of previous length and 1.
            else:                             #If count has more than k entries, subarray nums[j]...nums[i] has k + 1 different integers.
                count.pop(nums[j])            #Remove nums[j] from count.
                j += 1                        #Move forward j.
                length = 1                    #Refresh length.
            while count[nums[j]] != 1:        #The last j for nums[i] should be the first integer in sliding window whose count is 1. For k > last j, nums[k]...nums[i] does not have enough k different integers.
                length += 1                   #While j goes forward, increase length by 1.
                count[nums[j]] -= 1           #Decrease count[nums[j]], since current j is already out of sliding window.
                j += 1
            result += length                  #Add length to result.
        return result                         #Return result.
