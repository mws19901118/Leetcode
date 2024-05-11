class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        worker = sorted([(w / q, q) for w, q in zip(wage, quality)])    #Use the ratio of wage to quality and quality to represent each worker and sort by ratio in ascending order.
        qualitySum, qualityHeap = 0, []                                 #Initialize the quality sum and max quality heap for pay group.
        for i in range(k):                                              #For the first k workers, add their quality to quality sum and push quality to max quality heap(min heap of negative quality).
            qualitySum += worker[i][1]
            heapq.heappush(qualityHeap, -worker[i][1])
        minWage = qualitySum * worker[k - 1][0]                         #The wage for pay group of first k workers is the total quality multiplied by the largest ratio in pay group. Since we sort workers by ratio, so it's qualitySum * worker[k - 1][0].
        for i in range(k, len(worker)):                                 #For each or remaining workers, we calculate the wage of the pay group where the current worker has the largest ratio.
            qualitySum += worker[i][1] + heapq.heappop(qualityHeap)     #Update quality sum, adding quality of current worker and substracting the max quality in the heap.
            heapq.heappush(qualityHeap, -worker[i][1])                  #Add quality of current worker to max quality heap. 
            minWage = min(minWage, qualitySum * worker[i][0])           #Calculate wage and update minWage.
        return minWage                                                  #Return minWage.
