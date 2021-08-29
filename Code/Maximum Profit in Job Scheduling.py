class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sortedJobs = sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)])     #Sort jobs by starting time.
        sortedStartTime = [x[0] for x in sortedJobs]                                        #Separate out the list of sorted start time for binary search.
        dp = [0] * (len(sortedJobs) + 1)                                                    #Initialize dp array, dp[i] means the max profit of scheduling jobs in sortedJobs[i:].
        for i in reversed(range(len(sortedJobs))):                                          #Traverse sortedJobs backward.
            index = bisect_left(sortedStartTime, sortedJobs[i][1])                          #Find the index of first job whose start time is larger than or equal to the end time of current job. 
            dp[i] = max(sortedJobs[i][2] + dp[index], dp[i + 1])                            #dp[i] is the max of dp[i + 1] and dp[index] plus profit of current job.
        return dp[0]                                                                        #Return dp[0]
