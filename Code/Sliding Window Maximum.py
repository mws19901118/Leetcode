class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()                                            #Initalize a deque, which contains indexes of all possible numbers to be sliding window max and is sorted in non-ascending order.
        for i, x in enumerate(nums):                            #Traverse nums.
            if dq and dq[0] <= i - k:                           #If dq is not empty and the first index is out of sliding window, pop it from left.
                dq.popleft()
            while dq and nums[dq[-1]] <= x:                     #While dq is not empty and the number on last index of dq is smaller than current new number, pop tail of dq.
                dq.pop()
            dq.append(i)                                        #Append current index to dq.
            if i >= k - 1:                                      #If i >= k - 1, append current max, which is the number on first index, to result.
                result.append(nums[dq[0]])
        return result
