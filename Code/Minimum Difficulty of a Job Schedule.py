class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:                                                                    #If number of jobs are smaller than d, return -1 because cannot schedule jobs per day.
            return -1
        rangeMax = [[0 for _ in range(len(jobDifficulty))] for _ in range(len(jobDifficulty))]        #Initialize the range max in jobDifficulty[i:j + 1].
        for i in range(len(jobDifficulty)):                                                           #Pre-compute rangeMax.
            m = jobDifficulty[i]
            for j in range(i, len(jobDifficulty)):
                m = max(m, jobDifficulty[j])
                rangeMax[i][j] = m
        
        @cache                                                                                        #Cache result.
        def dp(k: int, d: int) -> int:                                                                #DP to find the minimum difficulty for jobDifficulty[:k] on d days.
            if d == 1:                                                                                #If d == 1, return max in jobDifficulty[:k].
                return rangeMax[0][k - 1]
            return min(dp(i, d - 1) + rangeMax[i][k - 1] for i in range(d - 1, k))                    #Otherwise, return the min for schedule jobDifficulty[:i] on d - 1 days and jobDifficulty[i:k] on d-th day.

        return dp(len(jobDifficulty), d)                                                              #Return dp(len(jobDifficulty), d).
