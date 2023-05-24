class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        t = sorted([(y, x) for x, y in zip(nums1, nums2)], reverse = True)      #Sort the tuple at same index by nums2 value in desending order.
        minHeap = [t[i][1] for i in range(k)]                                   #Create a min heap of size k, containing the first k tuples.
        heapq.heapify(minHeap)
        nums1Sum = sum(minHeap)                                                 #Sum it up to get the initial value of sum in nums1.
        result = nums1Sum * t[k - 1][0]                                         #Calculate the initial score of first k tuples.
        for x, y in t[k:]:                                                      #Traverse t[k:]; for each i, basically fixing the min number from nums2 at t[i] and use min heap to track the k largest numbers from nums1 in t[:i + 1],
            nums1Sum += y - heapq.heappop(minHeap)                              #Update nums1Sum by adding y and substracting the top of min heap.
            heapq.heappush(minHeap, y)                                          #Push y to min heap.
            result = max(result, nums1Sum * x)                                  #Calculate current score and update result if necessary.
        return result
