class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = sum(nums)                                                   #Calculate sum of nums.
        duplicate = 0
        for x in nums:                                                  #Traverse nums.
            if nums[abs(x) - 1] < 0:                                    #If nums[abs(x) - 1] is smaller than 0, abs(x) has already been visited, so abs(x) is the duplicate.
                duplicate = abs(x)
            else:                                                       #Otherwise convert nums[abs(x) - 1] to it's opposite number.
                nums[abs(x) - 1] *= -1
        missing = (len(nums) + 1) * len(nums) // 2 - s + duplicate      #Calculate the missing number: sum from 1 to n - s + duplicate.
        return [duplicate, missing]
