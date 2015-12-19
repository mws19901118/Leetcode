class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        fast = 0                                        #Use two pointers.
        slow = 0
        while fast < l:
            if nums[slow] == 0 and nums[fast] == 0:     #If nums[slow] is 0 and nums[fast] is 0, increasefast by 1.
                fast += 1
            elif nums[slow] == 0 and nums[fast] != 0:   #If nums[slow] is 0 and nums[fast] is not 0, swap the 2 number.
                nums[slow] = nums[fast]
                nums[fast] = 0
            else:                                       #Otherwise, increase both fast and slow by 1.
                fast += 1
                slow += 1
