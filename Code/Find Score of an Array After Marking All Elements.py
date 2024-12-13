class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = [(x, i) for i, x in enumerate(nums)]      #Put each number and its index in a min heap.
        heapq.heapify(heap)
        marked = set()                                   #Store marked index.
        score = 0
        while heap:                                      #Iterate while heap is not empty.
            x, i = heapq.heappop(heap)                   #Pop number and index from top of heap.
            if i not in marked:                          #If index is not marked, add the number to score and mark index and 2 adjacent indexes as marked.
                score += x
                marked.add(i)
                marked.add(i - 1)
                marked.add(i + 1)
        return score
