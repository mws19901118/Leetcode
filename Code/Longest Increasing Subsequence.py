class Solution(object):
    def lengthOfLIS(self, nums: List[int]) -> int:
        leastendelement = []                                        #The ith element stores the smallest ending element for increasing subsequence whose length is i.
        for x in nums:
            if leastendelement == [] or x > leastendelement[-1]:
                leastendelement.append(x)                           #If current element is greater than the ending element of current longest increasing subsequence, append current element to leastendelement.
            else:                                                   #Otherwise, binary search the smallest number in the least that is greater than current element and replace it with current element.
                start = 0
                end = len(leastendelement)
                while start < end:
                    mid = (start + end) // 2
                    if leastendelement[mid] >= x and (mid == 0 or leastendelement[mid - 1] < x):
                        leastendelement[mid] = x
                        break
                    elif leastendelement[mid] < x:
                        start = mid + 1
                    else:
                        end = mid - 1
        return len(leastendelement)                                 #Return the length of leastendelement.
