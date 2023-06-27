class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [(nums1[0] + nums2[0], 0, 0)]                                                #Use a min heap to store the sum of pair and its index in nums1 and nums2 respectively.
        visited = set()                                                                     #Store visited indexes pair in a hash set.
        result = []                                                                         #Initialize result list.
        while heap and k:                                                                   #Iterate while heap is not empty and k > 0.
            s, i, j = heapq.heappop(heap)                                                   #Pop heap top.
            if (i, j) in visited:                                                           #If indexes pair is visited, skip.
                continue
            visited.add((i, j))                                                             #Add indexes pair to visited.
            result.append([nums1[i], nums2[j]])                                             #Append the corresponding numbers at indexes pair to result.
            if i + 1 < len(nums1):                                                          #If i + 1 < len(nums1), move to i + 1 and push (nums1[i + 1] + nums2[j], i + 1, j) to heap.
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
            if j + 1 < len(nums2):                                                          #If j + 1 < len(nums2), move to j + 1 and push (nums1[i] + nums2[j + 1], i, j + 1) to heap.
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1                                                                          #Decrease k.
        return result
