class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minV, maxV = min(nums), max(nums)                                                                #Find the min value and max value in nums.
        distance_min = 0
        for i in range(len(nums)):                                                                       #Calculate the distance from the leftmost min value to the start of nums.
            if nums[i] == minV:
                break
            distance_min += 1
        distance_max = 0
        for i in reversed(range(len(nums))):                                                             #Calculate the distance from the rightmost min value to the end of nums.
            if nums[i] == maxV:
                break
            distance_max += 1
        return distance_min + distance_max - (1 if distance_min + distance_max >= len(nums) else 0)      #Return sum of distance_min and distance_max and minus one if distance_min + distance_max >= len(nums) because in this case min value and max value will cross each other and save a swap. 
