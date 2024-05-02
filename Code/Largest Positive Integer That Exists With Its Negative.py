class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)                                      #Store numbers in a set.
        for i in reversed(range(1, max(nums) + 1)):        #Traverse from the max number in nums to 1.
            if i in s and -i in s:                         #If both i and -i is in s, return i.
                return i
        return -1                                          #Return -1 if no such positive number.
