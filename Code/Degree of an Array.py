from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)                                                     #Count the frequency of each element,
        d = max(c.values())                                                   #Get the max frequency, aka the degree.
        n = filter(lambda x: c[x] == d, c)                                    #Filter out the elements having max frequency.
        r = nums[::-1]                                                        #Reverse the list.
        result = len(nums) + 1                                                #Initalize the result to be a number larger than list length.
        for x in n:                                                           #For each element in n, find the length of subarray which begins with the first index of the element and ends with the last index of the element.
            result = min(result, len(nums) - r.index(x) - nums.index(x))      #To calculate the last element, we find the first index in reversed list.
        return result
