class Solution:
    def maxScore(self, s: str) -> int:
        count = s.count("1")                                              #Count total 1s.
        score, curr_0 = 0, 0                                              #Initialize score and current count of 0.
        for i in range(len(s) - 1):                                       #Traverse all possible end of left substring.
            curr_0 += (s[i] == "0")                                       #Update current count of 0.
            score = max(score, curr_0 + (count - i - 1 + curr_0))         #Calculate current score and update score if necessary; 1s in right substring is count - (i + 1 - curr_0).
        return score
