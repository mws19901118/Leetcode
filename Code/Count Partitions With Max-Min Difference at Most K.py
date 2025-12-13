class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        division = 10 ** 9 + 7                                                          #Initialize division.
        dp = [1] + [0] * len(nums)                                                      #Store dp result; dp[i] is the partitions for nums[:i] and initially dp[0] is 1 as there is only 1 partition for itself.
        prefixSum = [1] + [0] * len(nums)                                               #Store the prefix sum of dp; same as dp, the initial value os 1.
        minQ, maxQ = deque(), deque()                                                   #Store the indexes of potential min value and max value in the sliding window.
        j = 0                                                                           #Initialize the left bound of sliding window.

        for i, x in enumerate(nums):                                                    #Traverse nums.
            while maxQ and nums[maxQ[-1]] <= x:                                         #Maintain a descending queue for max values.
                maxQ.pop()
            maxQ.append(i)

            while minQ and nums[minQ[-1]] >= x:                                         #Maintain a ascending queue for min values.
                minQ.pop()
            minQ.append(i)

            while maxQ and minQ and nums[maxQ[0]] - nums[minQ[0]] > k:                  #Shrink window size while the difference between max value and min value is greater than k.
                if maxQ[0] == j:
                    maxQ.popleft()
                if minQ[0] == j:
                    minQ.popleft()
                j += 1

            dp[i + 1] = (prefixSum[i] - prefixSum[j - 1]) % division                    #Update dp[i + 1], for every partition that ends between nums[j:i], we can add a new partition that ends at i.
            prefixSum[i + 1] = (prefixSum[i] + dp[i + 1]) % division                    #Update prefixSum[i + 1].

        return dp[-1]                                                                   #Return dp[-1].
