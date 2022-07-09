class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)                                    #Store the max score from current index to the end.
        dq = deque()                                            #Use a deque to store index of potential max score in a sliding window whose length is k.
        for i in reversed(range(len(nums))):                    #Traverse nums backwards.
            if dq and dq[0] > i + k:                            #If index of current max score in sliding window is beyond the reach from index i, pop it from dq.
                dq.popleft()
            dp[i] = nums[i] + (dp[dq[0]] if dq else 0)          #Calculate the max score from i.
            while dq and dp[dq[-1]] < dp[i]:                    #Pop all the indexes in dq whose score is smaller than current score, because they are no longer a max score in sliding window at anytime.
                dq.pop()
            dq.append(i)                                        #Append i to dq.
        return dp[0]                                            #Return the max score from index 0.
