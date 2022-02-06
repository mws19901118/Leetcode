class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2                                    #Initialize slow pointer at index 2.
        for fast in range(2, len(nums)):            #Traverse fast pointer from inedx 2 to end of nums.
            if nums[slow - 2] != nums[fast]:        #If nums[fast] is a number without duplicates more than 2, replace nums[slow] with nums[fast] and move forward slow pointer.
                nums[slow] = nums[fast]
                slow += 1
        return slow                                 #Return where slow pointer stops.
