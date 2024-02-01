class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()                              #Sort nums.
        result = []
        for i in range(0, len(nums), 3):         #Divide every 3 numbers.
            if nums[i + 2] - nums[i] > k:        #If the max difference between current 2 numbers are greater than k, return empty list.
                return []
            result.append(nums[i:i + 3])
        return result
