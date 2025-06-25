class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countSmaller(x: int) -> int:                                   #Calculate the number of products that are smaller than or euqal to x.
            count = 0                                                      #Initialize count.
            i, j = 0, index2 - 1                                           #Find in nums1[:index1] and nums2[:index2]. so initialize i to traverse nums1[:index1] forward and j to traverse nums2[:index2] backward.
            while i < index1 and j >= 0:
                if nums1[i] * nums2[j] > x:                                #If the product is greater than x, move forward i to go to next smaller product for nums2[j].
                    i += 1
                else:                                                      #Otherwise, all integers in nums1[i:index1] will have a product with nums2[j] that is smaller than or equal to x, so add index1 - i to count. Because for any integer y in nums1[i:index1], nums1[i] <= y < 0, since nums1[i] * nums2[j] <= x and nums2[j] < 0, then y * nums2[j] <= x.
                    count += index1 - i
                    j -= 1                                                 #Move backward j.
            i, j = index1, len(nums2) - 1                                  #Find in nums1[index1:] and nums2[index2:]. so initialize i to traverse nums1[index1:] forward and j to traverse nums2[index2:] backward.
            while i < len(nums1) and j >= index2:
                if nums1[i] * nums2[j] > x:                                #If the product is greater than x, move backward j to go to next smaller product for nums1[i].
                    j -= 1
                else:                                                      #Otherwise, all integers in nums2[index2:j + 1] will have a product with nums1[i] that is smaller than or equal to x, so add j - index2 + 1 to count. Because for any integer y in nums2[index2:j + 1], 0 <= y <= nums2[j], since nums1[i] * nums2[j] <= x and nums1[i] >= 0, then y * nums1[i] <= x.
                    count += j - index2 + 1
                    i += 1                                                 #Move forward i.
            i, j = 0, index2                                               #Find in nums1[:index1] and nums2[index2:]. so initialize i to traverse nums1[:index1] forward and j to traverse nums2[index2:] forward.
            while i < index1 and j < len(nums2):
                if nums1[i] * nums2[j] > x:                                #If the product is greater than x, move forward j to go to next smaller product for nums1[i].
                    j += 1
                else:                                                      #Otherwise, all integers in nums2[j:] will have a product with nums1[i] that is smaller than or equal to x, so add len(nums2) - j to count. Because for any integer y in nums2[j:], 0 <= nums2[j] <= y, since nums1[i] * nums2[j] <= x and nums1[i] < 0, then y * nums1[i] <= x.
                    count += len(nums2) - j
                    i += 1                                                 #Move forward i.
            i, j = index1, 0                                               #Find in nums1[index1:] and nums2[:index2]. so initialize i to traverse nums1[index1:] forward and j to traverse nums2[:index2] forward.
            while i < len(nums1) and j < index2:
                if nums1[i] * nums2[j] > x:                                #If the product is greater than x, move forward i to go to next smaller product for nums2[j].
                    i += 1
                else:                                                      #Otherwise, all integers in nums1[i:] will have a product with nums2[j] that is smaller than or equal to x, so add len(nums1) - i to count. Because for any integer y in nums1[i:], 0 <= nums1[i] <= y, since nums1[i] * nums2[j] <= x and nums2[j] < 0, then y * nums2[j] <= x.
                    count += len(nums1) - i
                    j += 1                                                 #Move forward j.
            return count

        index1, index2 = bisect_left(nums1, 0), bisect_left(nums2, 0)      #Find the indexes to insert 0 in each array respectively. Thus, nums1[:index1] and nums2[:index2] only contain sorted negative integers while nums1[index1:] and nums2[index2:] only contain sorted zero or positive integers. 
        start, end = -10 ** 10, 10 ** 10                                   #Find the lower bound and upper bound of product.
        while start <= end:                                                #Binary search.
            mid = (start + end) // 2
            if countSmaller(mid) < k:                                      #If there are fewer than k product smaller than mid, move start to mid + 1.
                start = mid + 1
            else:                                                          #Otherwise, move end to mid - 1
                end = mid - 1
        return start                                                       #Return start.
