class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0                                                              #Record the max length.
        boundary = {}                                                           #Store the mapping between lower and upper boundary
        for x in nums:                                                          #Traverse nums.
            if x in boundary:                                                   #Skip duplicates.
                continue
            lower = boundary[x - 1] if x - 1 in boundary else x                 #Get the lower boundary.
            upper = boundary[x + 1] if x + 1 in boundary else x                 #Get the upper boundary.
            boundary[x], boundary[lower], boundary[upper] = x, upper, lower     #Update lower and upper boundary. 
            length = max(length, upper - lower + 1)                             #Update max length.
        return length
