class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = 0x80000000              #Record the possible first value.
        b = 0x80000000              #Record the possible second value.
        for x in nums:              #Traverse through nums, we want a and b as small as possible.
            if x < a:               #If current value is smaller than a, replace a with current value.
                a = x
            elif x > a:
                if x < b:           #If current value is greater than a and smaller than b, replace b with current value.
                    b = x
                elif x > b:         #If current value is greater than b, an increasing triplet subsequence is found.
                    return True
        return False
