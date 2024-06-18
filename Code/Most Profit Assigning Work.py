class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort()                                                      #Sort worker.
        job = sorted((d, p) for d, p in zip(difficulty, profit))           #Sort job.
        result, i, maxProfit = 0, 0, 0                                     #Initialize result, the pointer to traverse job and the max profix in job[:i].
        for x in worker:                                                   #Traverse worker.
            while i < len(job) and job[i][0] <= x:                         #While job[i][o] <= x, meaning job[i] can be processed by current worker, update the max profit and move forward i.
                maxProfit = max(maxProfit, job[i][1])
                i += 1
            result += maxProfit                                            #Assign the job with max profit to current worker.
        return result
