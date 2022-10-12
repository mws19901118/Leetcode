class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)                               #Sort nums in desending order.
        for i in range(2, len(nums)):                           #Find the largest consecutive elements which can form a triangle, then return the sum of those 3.
            if nums[i - 2] < nums[i - 1] + nums[i]:             #Let's say they are a < b < c. If a + b <= c, then any a' and b' before a and b will have a' + b' <= c. Thus no valid triangle existed given the longest edge is c.
                return nums[i - 2] + nums[i - 1] + nums[i]      #Otherwise a + b > c, it's a valid triangle and any a' abd b' before a and b will have a' + b' <= a + b. Thus, a + b + c has the longest perimeter for the triagnle whose longest edge is c.
        return 0                                                #If no valid triangle found, return 0.
