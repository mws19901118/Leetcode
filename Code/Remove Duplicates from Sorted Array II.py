class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:                           #If nums length is smaller than 2, there is no duplicates.
            return len(nums)
        slow, fast = 2, 2                           #Start 2 pointers from the third number.
        while fast < len(nums):                     #Traverse fast pointer through nums.
            if nums[slow - 2] != nums[fast]:        #If nums[fast] is a number without duplicates more than 2, replace nums[slow] with nums[fast] and move forward slow pointer.
                nums[slow] = nums[fast]
                slow += 1
            fast += 1                               #Move forward fast pointer.
        return slow                                 #Return where slow pointer stops.
