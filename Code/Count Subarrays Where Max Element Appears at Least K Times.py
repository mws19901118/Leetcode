class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)                        #Find the max element in nums.
        count, start, result = 0, 0, 0                 #Initialize max element count in window, start of window and total result.
        for i, x in enumerate(nums):                   #Traverse nums.
            if x == max_element:                       #If x is max_element, increase count.
                count += 1
            while count == k:                          #Move forward start while count equals k to maintain a window which has less than k max elements.
                if nums[start] == max_element:         #If nums[start] is max_element, decrease count.
                    count -= 1
                start += 1
            result += start                            #For subarrays ending at i, the start of subarray has to be outside the window, so the number of valid subarraies is start.
        return result
