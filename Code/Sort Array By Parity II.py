class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1                                          #Initialize pointers of even index and odd index.
        while True:                                               #Traverse nums.
            while even < len(nums) and nums[even] & 1 == 0:       #While current number on even index is even, move forward even index.
                even += 2
            while odd < len(nums) and nums[odd] & 1 == 1:         #While current number on odd index is odd, move forward odd index.
                odd += 2
            if even < len(nums) and odd < len(nums):              #If both even and odd index is valid, swap the numbers on them.
                nums[even], nums[odd] = nums[odd], nums[even]
            else:                                                 #Otherwise, jump out of loop.
                break
        return nums                                               #Return nums.
