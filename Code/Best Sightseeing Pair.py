class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_score, result = 0, 0                        #Initialize the max score(value + index) so far and result.
        for i, x in enumerate(values):                  #Traverse values.
            result = max(result, max_score + x - i)     #Update result if max_score + x - i is larger.
            max_score = max(max_score, x + i)           #Update max score if necessary.
        return result
