class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        @cache                                                                                                 #Cache result.
        def canFinish(limit: int) -> bool:                                                                     #Check if the workers can finish within the time limit.
            return sum(floor((sqrt(1 + 8 * limit / t) - 1) / 2) for t in workerTimes) >= mountainHeight        #Sum up the max height each worker can remove in the time limit. For each worker time t, suppose x is the height, then t * x * (x + 1) // 2 <= limit => x * x + x - 2 * limit / t <= 0. Accoding to the quadratic formula, the approximate value of x is floor((sqrt(1 + 8 * limit / t) - 1) / 2).

        start, end = 1, 5000050000000000                                                                       #Initailize the lower and upper boundries to be 1 and 5000050000000000(when we have highest height is 100000 and 1 slowest worker in workerTimes [1000000]).
        while start <= end:                                                                                    #Binary search.
            mid = (start + end) // 2
            if canFinish(mid) and not canFinish(mid - 1):
                return mid
            elif canFinish(mid - 1):
                end = mid - 1
            else:
                start = mid + 1
