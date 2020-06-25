class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start, end = 1, len(nums) - 1                           #The numbers ranges from 1 to n.
        while start < end:                                      #Binary search for the answer in 1 to n.
            mid = (start + end) // 2
            count = sum(x <= mid for x in nums)                 #Count how many numbers in nums are smaller than or equal to mid.
            if count <= mid:                                    #If the count is no larger than mid, there can not be any duplicates number from 1 to mid, binary search in mid+1 to n.
                start = mid + 1
            else:                                               #Otherwise, the duplicates number must be between 1 and mid, binary search in 1 to mid.
                end = mid
        return start
