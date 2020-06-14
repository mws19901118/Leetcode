class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()                                                               #Sort nums.
        subsets = []                                                              #Store the data of the max subset ending at each position.
        maxSet = (0, -1, -1)                                                      #Record largest subset. Using the format of (length, previous num position, current num value).
        for i, x in enumerate(nums):                                              #Traverse through the list.
            currentSet = (1, -1, x)                                               #Record current subset. -1 means no previous num.
            for j, y in enumerate(nums[:i]):                                      #Iterate each num before current num.
                if x % y == 0 and subsets[j][0] + 1 > currentSet[0]:              #If there are divisible and the new-formed subset is larger than current subset, update current subset.
                    currentSet = (subsets[j][0] + 1, j, x)
            subsets.append(currentSet)                                            #Add current subset to the subset list.
            if currentSet[0] > maxSet[0]:                                         #Update largest subset.
                maxSet = currentSet
                
        result = []                                                               #Result list.
        while nums:                                                               #Iterate while nums has value(handle the situation where nums is empty).
            result.append(maxSet[2])                                              #Add current num value to result.
            if maxSet[1] == -1:                                                   #If no previous value, break.
                break
            else:                                                                 #Backtracking each num in subset.
                maxSet = subsets[maxSet[1]]
        return result
