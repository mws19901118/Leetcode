class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pairSum = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])      #It's basically dividing weights into k subarrays.
        return 0 if k == 1 else (sum(pairSum[-(k - 1):]) - sum(pairSum[:k - 1]))              #However, only the start and end of each subarray counts for score.
                                                                                              #Also, both the start of first subarray and end of last subarray is fixed.
                                                                                              #The score is sum of k - 1 adjacent pairs in weights.
                                                                                              #Calculate all adjacent paris and sort them.
                                                                                              #If k == 1, return 0, as the subarray is weight it self.
                                                                                              #Otherwise, return the difference between last k - 1 pairs(max score) and first k - 1 pairs(min score).
