class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()                                      #Sort nums.
        if nums[0] + nums[1] <= nums[2]:                 #Check if cannot make a triangle; if so, return "none".
            return "none"
        if nums[0] == nums[1] == nums[2]:                #Check if is equilateral triangle; if so, return "equilateral".
            return "equilateral"
        if nums[0] == nums[1] or nums[1] == nums[2]:     #Check if is isosceles triangle; if so, return "isosceles".
            return "isosceles"
        return "scalene"                                 #Return "scalene".
