class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        lastIndexes = defaultdict(list)                #Store the last index of each number in sliding window; its size is at most 3.
        left, result = -1, 0                           #Initialize the left boundary(not inclusive) of sliding window as well as result.
        for i, x in enumerate(nums):                   #Traverse nums.
            keys = list(lastIndexes.keys())            #Copy numbers in sliding window.
            for y in keys:                             #Traverse numbers.
                if abs(x - y) > 2:                     #If its distance from x is greater than 2, move left to its last index then pop it from last indexes.
                    left = max(left, lastIndexes[y])
                    lastIndexes.pop(y)
            lastIndexes[x] = i                         #Update the last index of x.
            result += i - left                         #For all the number in sliding window, there is a continous subarray starting at there and ending at x.
        return result
