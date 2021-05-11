class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        slidingWindowSum = sum(cardPoints[:k])                          #Maintain the sum of a sliding window with length k.
        maxPoints = slidingWindowSum                                    #Initial max points is the initial sliding window sum.
        for i in range(1, k + 1):                                       #Slide the window backward from first k in the front to last k in the end.
            slidingWindowSum += cardPoints[-i] - cardPoints[k - i]      #Update sliding window sum.
            maxPoints = max(maxPoints, slidingWindowSum)                #Update max points.
        return maxPoints                                                #Return max points.
