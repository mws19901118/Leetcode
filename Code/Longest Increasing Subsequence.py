class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        l = len(nums)
        leastendelement = [nums[0]]                                 #The ith element stores the smallest ending element for increasing subsequence whose length is i.
        for i in range(1, l):
            if nums[i] > leastendelement[-1]:
                leastendelement.append(nums[i])                     #If current element is greater than the ending element of current longest increasing subsequence, append current element to leastendelement.
            else:                                                   #Otherwise, binary search the smallest number in the least that is greater than current element and replace it with current element.
                start = 0
                end = len(leastendelement)
                while start < end:
                    mid = (start + end) / 2
                    if leastendelement[mid] >= nums[i] and (mid == 0 or leastendelement[mid - 1] < nums[i]):
                        leastendelement[mid] = nums[i]
                        break
                    elif leastendelement[mid] < nums[i]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return len(leastendelement)                                 #Return the length of leastendelement.
