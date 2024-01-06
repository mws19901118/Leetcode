class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])           #Sort jobs by starting time.
        dp = [0] * (len(sortedJobs) + 1)                                                    #Initialize dp array, dp[i] means the max profit of scheduling jobs in sortedJobs[i:].
        for i, (s, e, p) in enumerate(reversed(jobs)):                                      #Traverse sortedJobs backward.
            index = bisect_left(jobs, (e, -1, -1))                                          #Find the index of first job whose start time is larger than or equal to the end time of current job. 
            dp[-(i + 2)] = max(p + dp[index], dp[-(i + 1)])                                 #dp[-(i + 2)] is the max of dp[-(i + 1)] and dp[index] plus profit of current job.
        return dp[0]                                                                        #Return dp[0]
