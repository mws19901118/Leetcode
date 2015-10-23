class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1                         #The numbers ranges from 1 to n.
        end = len(nums) - 1
        while start < end:                #Binary search for the answer in 1 to n.
            mid = (start + end) / 2
            count = 0
            for i in nums:                #Count how many numbers in nums are smaller than or equal to mid.
                if i <= mid:
                    count += 1
            if count <= mid:              #If the count is no larger than mid, there can not be any duplicates number from 1 to mid, binary search in mid+1 to n.
                start = mid + 1
            else:                         #Otherwise, the duplicates number must be between 1 and mid, binary search in 1 to mid.
                end = mid
        return start
