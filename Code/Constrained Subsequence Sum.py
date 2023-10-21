class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()                                       #Use a dq to store the useful index of dp for future calculation and keep the dp values monotonic dereasing.
        dp = [0] * len(nums)                              #Store the max constrained subsequence sum ending at each index.
        for i, x in enumerate(nums):                      #Traverse nums.
            if q and i - q[0] > k:                        #While queue and the head of queue is more than k distance away from i, pop it from queue.
                q.popleft()
            dp[i] = (dp[q[0]] if q else 0) + x            #Calculate dp[i]; by default it is x, if q is not empty, add dp[q[0]] to x.
            while q and dp[q[-1]] < dp[i]:                #While queue is not empty and dp[q[-1]] is smaller than current dp[i], they are not useful for future calculation, pop them from queue.
                q.pop()
            if dp[i] > 0:                                 #If current dp[i] is greater than 0, append i to q.
                q.append(i)
        return max(dp)                                    #Return max of dp.
