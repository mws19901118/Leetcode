class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scores = [s for a,s in sorted(zip(ages, scores))]                   #Sort score by ages asending then scores ascending.
        dp = copy.deepcopy(scores)                                          #Deepcopy scores to be dp; dp[i] means the max score in scores[:i + 1] with picking scores[i].
        for i in range(len(scores)):                                        #Traverse scores from beginning. 
            for j in range(i):                                              #Traverse from 0 to i - 1.
                if scores[j] <= scores[i]:                                  #If scores[j] <= scores[i], update dp[i] if dp[j] + scores[i] is greater.
                    dp[i] = max(dp[i], dp[j] + scores[i])
        return max(dp)                                                      #Return the max of dp.
