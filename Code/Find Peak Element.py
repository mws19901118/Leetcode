class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        nums.insert(0, -0x8fffffff)                                         #Add a negative max in the start.
        nums.append(-0x8fffffff)                                            #Add a negative max in the end.
        start = 1
        end = l
        while start <= end:                                                 #Do binary search from 1 to l.
            mid = (start + end) / 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:     #If nums[mid] is a peak element, return mid - 1(becase we added a nagative max in the start).
                return mid - 1
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:   #If it's in a rising subarray, there must be at least 1 peak element in the second half.
                start = mid + 1
            else:                                                           #Otherwise, there must be at least 1 peak element in the first half.
                end = mid - 1
