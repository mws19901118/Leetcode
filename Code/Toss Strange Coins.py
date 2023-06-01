class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        @cache                                                                                                    #Cache result.
        def dp(index: int, x: int):                                                                               #Calculate the probability of facing x heads by tossing prob[index:] coins.
            if index == len(prob):                                                                                #If index == len(prob), it reaches the end, return 1 if x is 0; return 0 otherwise.
                return 1 if not x else 0
            if x < 0 or x > len(prob) - index:                                                                    #If x < 0 or x > len(prob) - index, it's absolutely impossible to face x heads, so return 0.
                return 0
            return prob[index] * dp(index + 1, x - 1) + (1 - prob[index]) * dp(index + 1, x)                      #There are 2 scenarios: 1. current coin faces head and prob[index + 1:] face x - 1 heads; 2. current coin faces tail and prob[index + 1:] face x heads. Return the sum of 2 probabilities. 

        return dp(0, target)                                                                                      #Return dp(0, target).
