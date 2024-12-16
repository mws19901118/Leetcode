class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        @cache                                                                                      #Cache result.
        def delta(nominator: int, denominator: int) -> float:                                       #Calculate the delta for (nominator + 1) / (denominator + 1) - nominator / denominator.
            return (denominator - nominator) / (denominator * (denominator + 1))
        
        heap = [(-delta(p, t), p, t) for p, t in classes]                                           #Put current pass and total in a max heap order by the delta after assigning an extra brilliant student.
        heapq.heapify(heap)
        for _ in range(extraStudents):                                                              #Iterate extraStudents times.
            _, p, t = heapq.heappop(heap)                                                           #Pop the class with max delta.
            heapq.heappush(heap, (-delta(p + 1, t + 1), p + 1, t + 1))                              #Assign one extra brilliant student to the class and push the class back to heap.
        return sum(nominator / denominator for _, nominator, denominator in heap) / len(heap)       #Calculate average pass ratio and return.
