class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)        #Sort nums in desending order.
        s = sum(nums)                    #Sum all numbers up.
        for x in nums:                   #Traverse nums/
            if s - x > x:                #If the sum of rest numbers(not including current number) is greater than current one, we can form a polygon and it has the largest perimeter, so we can return it.
                return s
            s -= x                       #Deduct current number from s. 
        return -1                        #Return -1 if we cannot found at last.
