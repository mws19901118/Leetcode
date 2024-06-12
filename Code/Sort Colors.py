class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, start, end = 0, 0, len(nums) - 1
        while i <= end:
            if nums[i] == 1:                                            #If current value is 1, simply increase i by 1.
                i += 1
            elif nums[i] == 0:                                          #If current value is 0, to move it to front, swap nums[i] with nums[start] and increase start by 1.
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                i += 1                                                  #We have to increase i by 1 here , because all the value in front of i is no greater than nums[i], if we don't do this, it may result in incorrect growth of start and index out of bound.
            else:                                                       #If current value is 2, to move it to end, swap nums[i] with nums[end] and decrease end by 1.
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
