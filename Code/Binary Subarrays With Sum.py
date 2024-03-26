class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def slidingWindowAtMost(nums: List[int], goal: int) -> int:                                #Count the number of subarrays with sum at most the given goal.
            start, current_sum, count = 0, 0, 0                                                    #Initialize start of sliding window, current sum and count of subarrays.
            for i in range(len(nums)):                                                             #Iterate through the array using a sliding window approach.
                current_sum += nums[i]                                                             #Add nums[i] to current_sum.
                while start <= i and current_sum > goal:                                           #Move the start to the right until the sum becomes less than or equal to the goal.
                    current_sum -= nums[start]
                    start += 1
                count += i - start + 1                                                             #Add the length of the current subarray to count.
            return count
        return slidingWindowAtMost(nums, goal) - slidingWindowAtMost(nums, goal - 1)               #Return the result of slidingWindowAtMost(nums, goal) - slidingWindowAtMost(nums, goal - 1).
