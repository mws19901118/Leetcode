class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []                                                                  #Use a min heap to store current fraction for each denominator, because arr is sorted, for each denominator, nominator increases from start to end.
        for i in range(1, len(arr)):                                               #Initially, nominator is 1 for all denominator.
            heapq.heappush(heap, (1 / arr[i], 0, i))                               #Push the fraction, nominator index and denominator index to heap.
        for _ in range(k - 1):                                                     #Pop heap k - 1 times.
            _, i, j = heapq.heappop(heap)
            if i + 1 < j:                                                          #If i + 1 < j, next fraction of current denominator is arr[i + 1] / arr[j]; Add fraction, nominator index and denominator index to heap.
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))
        return [arr[heap[0][1]], arr[heap[0][2]]]                                  #The heap top is the k-th smallest prime fraction. Return nominator and denominator given their indexes.
