class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        start, end = max(nums), sum(nums)     #Binary seach for the satisfied anwser.
        result = end                          #Since the least number of subarray is 1, so start from the max number in array.
        while start <= end:                   #Also, if m = 1, then the least sum is the sum of array, so end with the sum of array.
            mid = (start + end) // 2          #Find the mid value between start and end.
            s = 0                             #Store the temp sum.
            count = 1                         #Count the number of subarray whose sum is not larger than mid.
            for x in nums:                    #Traverse the array to split the array as less as possible so the sum of each subarray is no larger than mid.
                if s + x > mid:
                    count += 1
                    s = x
                else:
                    s += x
            if count > m:                     #If the total satisfied subarrays are more than m, continue binary search from mid + 1 to end.
                start = mid + 1
            else:                             #Otherwise, update result to find the least satisfied result and keep binary search from start to mid - 1.
                result = min(result, mid)
                end = mid - 1
        return result
