class Solution:
    def findElement(self, nums1, nums2, k):                         #Find the k-th number in two sorted non-descending array.
        if len(nums1)>len(nums2):                                   #Ensure that nums1 is not longer than nums2 by switching nums1 and nums2 when nums1 is longer than nums2.
            return self.findElement(nums2, nums1, k)
        if len(nums1)==0:                                           #If nums1 is empty, return the k-th number of nums2.
            return nums2[k-1]
        if k==1:                                                    #If k is 1, return the smaller one of nums1[0] and nums[2].
            return min(nums1[0],nums2[0])
        k1=min(k/2,len(nums1))                                      #Divide k into 2 integers, k1 and k2, which are approximately equal and ensure k1 is not greater than the length of nums1.
        k2=k-k1                                                     #Ensure k1+k2=k.
        if nums1[k1-1]==nums2[k2-1]:                                #If nums1[k1-1]=nums2[k2-1], return the value of nums1[k1-1], which is the k-th number of nums1 and nums2.
            return nums1[k1-1]
        elif nums1[k1-1]<nums2[k2-1]:                               #If nums1[k1-1]<nums2[k2-1], nums1[k1-1] can't be the k-th number. Because the first k1 numbers of nums1 are certainly smaller than the k-th number, we can ignore them and find the k2-th number in nums2 and the remaining nums1.
            return self.findElement(nums1[k1:], nums2, k2)
        else:                                                       #If nums1[k1-1]>nums2[k2-1], nums2[k2-1] can't be the k-th number. Because the first k2 numbers of nums2 are certainly smaller than the k-th number, we can ignore them and find the k1-th number in nums1 and the remaining nums2.
            return self.findElement(nums1, nums2[k2:], k1)
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        l1=len(nums1)
        l2=len(nums2)
        if (l1+l2)%2==1:                                            #If the total amount of numbers n is odd, find the n/2-th number of nums1 and nums2.
            return self.findElement(nums1,nums2,(l1+l2)/2+1)
        else:                                                       #If the total amount of numbers n is even, find the mean of n/2-th number and n/2+1-th number of nums1 and nums2.
            return (self.findElement(nums1,nums2,(l1+l2)/2)+self.findElement(nums1, nums2, (l1+l2)/2+1))/2.0
