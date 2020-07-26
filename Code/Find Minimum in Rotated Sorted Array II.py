class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        start, end = 0, len(nums) - 1
        while start < end and nums[start] >= nums[end]:     #Binary search. If nums[start] < nums[end], it's already asending from start to end, stop binary search.
            mid = (end + start) // 2
            if nums[mid] > nums[start]:                     #If nums[mid] > nums[start], min element is on the right of mid.
                start = mid + 1
            elif nums[mid] < nums[start]:                   #if nums[mid] < nums[start], min element is either mid or on the left of mid.
                end = mid
            else:                                           #Can not discard either branch. Thus, it goes O(n) in such case.
                start += 1
        return nums[start]
