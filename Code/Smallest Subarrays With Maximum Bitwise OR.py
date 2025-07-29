class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        or_result = reduce(lambda x, y: x | y, nums)                         #Calculate the or result for entire nums.
        mask = 1                                                             #Initialize bit mask at 1.
        bits = {}                                                            #Store the smallest index of the number containing the bit mask in key during traverse.
        while mask <= or_result:                                             #Shift left mask until it is greater than or_result.
            if mask & or_result:                                             #If current bit mask is in or_result, set the index of current bit mask to the length of nums.
                bits[mask] = len(nums)
            mask <<= 1
        current_or = 0                                                       #Initialize current or result to traverse.
        result = [0] * len(nums)                                             #Initialize result.
        for i in reversed(range(len(nums))):                                 #Traverse nums in backward.
            current_or |= nums[i]                                            #Update current or result.
            for b in bits:                                                   #Traverse bit masks and update its min index if current number has this bit mask.
                if b & nums[i]:
                    bits[b] = i
            indexes = [bits[b] for b in bits if b & current_or]              #Find the indexes of each bit mask in current or result.
            result[i] = 1 if not indexes else max(indexes) - i + 1           #If the indexes list is empty, set result[i] to 1 because it means all numbers in nums[i:] are 0; otherwise, max(indexes) - i + 1 is the min length of subarray starting at i which can generate current or result, 
        return result
