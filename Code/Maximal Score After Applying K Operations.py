class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]                         #Store nums in max heap.
        heapq.heapify(heap)
        score = 0
        for _ in range(k):                                #Iterate k times.
            x = -heapq.heappop(heap)                      #Pop heap top.
            score += x                                    #Add the value to score.
            heapq.heappush(heap, -ceil(x / 3))            #Push back ceil(x / 3) to heap.
        return score
