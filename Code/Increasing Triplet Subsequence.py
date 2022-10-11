class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a, b = float('inf'), float('inf')               #Record the possible first and second value.
        for x in nums:                                  #Traverse through nums, we want a and b as small as possible.
            if x < a:                                   #If current value is smaller than a, replace a with current value.
                a = x
            elif a < x < b:                             #If current value is greater than a and smaller than b, replace b with current value.
                b = x
            elif b < x:                                 #If current value is greater than b, an increasing triplet subsequence is found.
                return True
        return False
