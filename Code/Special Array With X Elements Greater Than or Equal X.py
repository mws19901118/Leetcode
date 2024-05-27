class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()                                                    #Sort nums in asending order.
        for i, x in enumerate(nums):                                   #Traverse nums.
            count = len(nums) - i                                      #Count all the numbers that are greater than or equal to x.
            if count <= x and (i == 0 or count > nums[i - 1]):         #If count <= x and either x is the first element or count is greater than nums[i = 1], there are exactly count elements greater than or equal to count.
                return count                                           #So, return count.
        return -1                                                      #Return -1 if no such element found.
