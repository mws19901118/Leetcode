class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result, left = 0, -1                                                #Initialize result and left boundary(not inclusive) of sliding window.
        minDeque, maxDeque = deque(), deque()                               #Use 2 deques to store the possible max and min values in sliding window and its index.
        for i, x in enumerate(nums):                                        #Traverse nums.
            if minDeque and minDeque[0][0] > x:                             #If minDeque is not empty and the first value is greater than x, x is the new min value in sliding window.
                while maxDeque and maxDeque[0][0] > x + limit:              #Popleft max deque if it is not empty and its first value if its distance to x is greater than limit.
                    left = maxDeque.popleft()[1]                            #Also update the left to the index of popped value.
            elif maxDeque and maxDeque[0][0] < x:                           #If maxDeque is not empty and the first value is smaller than x, x is the new max value in sliding window.
                while minDeque and minDeque[0][0] < x - limit:              #Popleft min deque if it is not empty and its first value if its distance to x is greater than limit.
                    left = minDeque.popleft()[1]                            #Also update the left to the index of popped value.
            result = max(result, i - left)                                  #Now the sliding window is nums[left + 1:i + 1], update result if necessary.
            while minDeque and minDeque[-1][0] > x:                         #While min deque is not empty and its last value is greater than x, pop the last value because it is no longer a candidate for min value.
                minDeque.pop()
            minDeque.append((x, i))                                         #Append x and i to min deque.
            while maxDeque and maxDeque[-1][0] < x:                         #While max deque is not empty and its last value is smaller than x, pop the last value because it is no longer a candidate for max value.
                maxDeque.pop()
            maxDeque.append((x, i))                                         #Append x and i to max deque.
        return result
