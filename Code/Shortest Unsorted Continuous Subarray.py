class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = -1, -1                                         #The array can be split into 3 subarrays, ABC. A and C are sorted while B is unsorted. Store the start and end index of B, initially -1 and -1.
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:         #Find the length of ascending array A' starting from beginning.
            i += 1
        if i == len(nums) - 1:                                      #If the entire array is already asending, return 0.
            return 0
        minV = min(nums[i + 1:])                                    #Get the min value of the remaining array.
        for j in range(i + 1):                                      #Set start to the first index in A' where its value is greater than minV.
            if nums[j] > minV:                                      #After sort, minV will be placed at start and every number before it won't change, so start is the actual start indxe of array B.
                start = j
                break
        i = len(nums) - 1                                           #Do the same from behind to get end.
        while i > 0 and nums[i] >= nums[i - 1]:
            i -= 1
        maxV = max(nums[:i + 1])
        for j in range(len(nums) - 1, i - 1, - 1):
            if nums[j] < maxV:
                end = j
                break
        return end - start + 1                                      #Return the length, which is end - start + 1.
