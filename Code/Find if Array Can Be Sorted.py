class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max, i = 0, 0                                                              #Initialize max of previous segment and a pointer to traverse nums.
        while i < len(nums):                                                            #Iterate while i hasn't reached the end.
            curr_max, curr_min, j = nums[i], nums[i], i                                 #Initialize max and min of current segment and a pointer to move forward for current segment.
            while j < len(nums) and nums[j].bit_count() == nums[i].bit_count():         #While nums[j] has the same set bits of nums[i] and hasn't reached the end, update curr_max and curr_min and move forward j.
                curr_max, curr_min = max(curr_max, nums[j]), min(curr_min, nums[j])
                j += 1
            if curr_min < prev_max:                                                     #If curr_min is smaller than prev_max, return false, because the operation can only sort segment in which elements all have same set bits.
                return False
            prev_max, i = curr_max, j                                                   #Update prev_max to curr_max and move i to j.
        return True                                                                     #Return true at the end.
