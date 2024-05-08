class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        result = [""] * len(score)                                                        #Initialize result.
        sortedScore = sorted([(x, i) for i, x in enumerate(score)], reverse = True)       #Sort in desending order and keep original index.
        for i, (x, index) in enumerate(sortedScore):                                      #Traverse and populate result.
            if i == 0:
                result[index] = "Gold Medal"
            elif i == 1:
                result[index] = "Silver Medal"
            elif i == 2:
                result[index] = "Bronze Medal"
            else:
                result[index] = str(i + 1)
        return result
            
