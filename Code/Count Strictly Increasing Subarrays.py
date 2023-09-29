class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ount, current = 0, 0                                                    #Initialize total count and count of strictly increasing subarray ending at current number.
        for i, x in enumerate(nums):                                            #Traverse nums.
            current = 1 if i == 0 or nums[i - 1] >= x else current + 1          #If i == 0 or nums[i - 1] >= x, current should be 1; otherwise increase 1 to current.
            count += current                                                    #Add current to count.
        return count
