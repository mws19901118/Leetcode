class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        @cache                                                                                                #Cache result.
        def canFit(x: int):                                                                                   #Determine if we can form a valid nums array with nums[index] == x.
            leftSpan = min(x - 1, index)                                                                      #Becase the max diff between adjacent numbers is 1 and we try not to waste any number, so calculate the span needed to get x from left. 
            leftSum = (x - 1 + x - leftSpan) * leftSpan // 2 + max(0, index - leftSpan)                       #Calculate the total sum on the left: use arithmetic sequence sum calculation for numbers in the left span while numbers outside left span should all be 1.
            rightSpan = min(x - 1, n - 1 - index)                                                             #Do the same for the right side.
            rightSum = (x - 1 + x - rightSpan) * rightSpan // 2 + max(0, n - 1 - index - rightSpan)
            return leftSum + rightSum + x <= maxSum                                                           #Return if we can fit all numbers within maxSum.       

        start, end = 0, maxSum
        while start <= end:                                                                                   #Binary search for the max value at nums[index].
            mid = (start + end) // 2
            if canFit(mid) and not canFit(mid + 1):
                return mid
            elif canFit(mid + 1):
                start = mid + 1
            else:
                end = mid - 1
