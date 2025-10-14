class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        length = [0] * len(nums)                                                                #Initialize the max strictly increasing subarray length starting at each index.
        i = 0
        while i < len(nums):                                                                    #Traverse nums.
            j = i + 1
            while j < len(nums) and nums[j] > nums[j - 1]:                                      #Use 2 pointers to find the max strictly increasing subarray length starting at i.
                j += 1
            while i < j:                                                                        #Populate the length for index from i to j - 1.
                length[i] = j - i
                i += 1
        return any(length[i] >= k and length[i + k] >= k for i in range(len(nums) - k))         #Return true if there are any index i that length[i] >= k and length[i + k] >= k.
