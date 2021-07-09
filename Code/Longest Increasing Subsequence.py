class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subsequence = []                                    #The ith element stores the smallest ending element for increasing subsequence whose length is i.
        for x in nums:                                      #Traverse nums.
            if not subsequence or subsequence[-1] < x:      #If current longest increasing subsequence is empty or its last element is smaller than x, append x to subsequence.
                subsequence.append(x)
            else:                                           #Otherwise, Binary search the first index to insert x in subsequence and still keep it sorted and replace the element in that index with x.
                index = bisect_left(subsequence, x) 
                subsequence[index] = x
        return len(subsequence)                             #Return the length of subsequence.
