class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()                                            #Initalize a deque, which contains all possible numbers to be sliding window max and is sorted in non-ascending order.
        for i, x in enumerate(nums):                            #Traverse through nums.
            if i >= k and nums[i - k] == dq[0]:                 #If i >= k and nums[i - k] eqauls the current max, pop it from left.
                dq.popleft()
            while dq and dq[-1] < x:                            #While dq is not empty and the tail of dq is smaller than current new number, pop tail of dq.
                dq.pop()
            dq.append(x)                                        #Append current new number to dq.
            if i >= k - 1:                                      #If i >= k - 1, append current max to result.
                result.append(dq[0])
        return result
