class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result, left, slidingWindowSum, maxSlidingWindowSum = 0, 0, 0, 0            #Initialize result, left pointer of sliding window, sliding window sum and max sliding window sum.
        for i, (x, y) in enumerate(zip(grumpy, customers)):                         #Traverse grumpy and customers together.
            if not x:                                                               #If current minute owner is not grumpy, add the customer in current minute to result and continue.
                result += y
                continue
            while left + minutes <= i:                                              #While left is out of the sliding window ending at current minute with length minutes, move forward left and update sliding window sum.
                slidingWindowSum -= grumpy[left] * customers[left]
                left += 1
            slidingWindowSum += y                                                   #Add the customer in current minute to sliding window sum.
            maxSlidingWindowSum = max(maxSlidingWindowSum, slidingWindowSum)        #Update the max sliding window sum if necessary.
        return result + maxSlidingWindowSum                                         #Return result + maxSlidingWindowSum.
