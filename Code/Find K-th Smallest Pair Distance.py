class Solution:
    def possible(self, nums, guess, k):
        count = left = 0                            #Count the pairs whose distance is not larger than guess.
        for right, x in enumerate(nums):            #Traverse through nums.
            while x - nums[left] > guess:           #For each index right, maintain left, the smallest value such that nums[right] - nums[left] <= guess.
                left += 1                           #So for all the pairs whose right boundary is right, and left bondary is between left and right, the distance is not larger than guess.
            count += right - left                   #Update count for each right.
        return count >= k                           #Return if count is equal to or larger than k.
    
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()                                 #Sort nums.
        start, end = 0, nums[-1] - nums[0]          #Binary search for anwser, starting from 0 and ending at the max distance in nums.
        while start < end:
            mid = (start + end) >> 1
            if self.possible(nums, mid, k):         #Determine if mid is possible to be equal to or larger than the k-th smallest pair distance.
                end = mid                           #If so, binary search from start to mid to find a smaller solution.
            else:                                   #Othwise, binary search from mid + 1 to end.
                start = mid + 1

        return start                                #Return start after binary search.
