class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        last = -1                                                                                            #Store the last k-distance index, initially -1.
        result = []
        for i, x in enumerate(nums):                                                                         #Traverse nums.
            if x == key:                                                                                     #Process if x is key.
                result.extend(j for j in range(max(last + 1, i - k), min(len(nums), i + k + 1)))             #Add all indexes from max(last + 1, i - k) to min(len(nums) - 1, i + k) inclusive to result.
                last = i + k                                                                                 #Update last.
        return result
