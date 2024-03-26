class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()                                     #Sort tokens.
        score, maxscore = 0, 0                            #Store current score and max score.
        start, end = 0, len(tokens) - 1                   #Two pointers from 2 ends.
        while start <= end:                               #Start traversal.
            if P < tokens[start]:                         #If P is smaller than token at start, cannot gain more score, so stop.
                break
            while start <= end and tokens[start] <= P:    #While P is larger than or eqaul to token at start, keep playing token at start face up and gaining score.
                P -= tokens[start]
                score += 1
                start += 1
            maxscore = max(maxscore, score)               #Update max score.
            if start <= end and score > 0:                #If token at end is available, play token at end face down and gain power.
                P += tokens[end]
                score -= 1
                end -= 1
        return maxscore                                   #Return max score.
