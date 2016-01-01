class Solution(object):
    def getMax(self, nums, k):                                                                        #Find the max length-k-number keeping the relative order of digits in nums.
        r = []                                                                                        #Use a stack to store digits.
        l = len(nums)
        for x in range(l):                                                                            #Check every digit in nums.
            while r != [] and len(r) + l - x > k and r[-1] < nums[x]:                                 #If r is not empty and the top of stack is smaller than current digit and there are still enough digits, pop the stack.
                r.pop()
            if len(r) < k:                                                                            #if we haven't added enough digits in stack, append current digit to stack.
                r.append(nums[x])
        return r                                                                                      #Return stack.
    
    def merge(self, a, b):                                                                            #Find the max number composed by digits in 2 sub numbers.
        return [max(a, b).pop(0) for i in a + b]                                                      #Pop the maxlarger one of the 2 first digits and store it in a list until there is no digits.
        
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):                                               #Divide k into 2 parts and find length-i-number and length-(k-i)-number in nums1 and nums2 respectively.
                result = max(result, self.merge(self.getMax(nums1, i), self.getMax(nums2, k - i)))    #Merge the results and keep the largest one.
        return result
