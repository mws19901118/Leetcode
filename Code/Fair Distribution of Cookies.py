class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        count = [0] * k                                                                                      #Initialize candies distributed to each kid.
        
        def backtracking(i: int, zeroCount: 0) -> int:                                                       #Backtracking.
            if len(cookies) - i < zeroCount:                                                                 #If number of candy bags left are smaller than kid that haven't been distributed any candy, return inifinite as it's for sure not an optimal distribution because at least one kid got more than one bag while there are kids cannot get any.
                return float('inf')
            if i == len(cookies):                                                                            #When all candy bags are distrubuted, return max(count) which is the unfairness of current distribution.
                return max(count)
            unfaireness = float('inf')                                                                       #Initialize unfaireness.
            for j in range(k):                                                                               #Try to distribute current bag to each kid.
                count[j] += cookies[i]                                                                       #Add cookies[i] to count[j].
                unfaireness = min(result, backtracking(i + 1, zeroCount - int(count[j] == cookies[i])))      #Keep backtracking with updated zeroCount for next iteration.
                count[j] -= cookies[i]                                                                       #Restore count[j].
            return unfaireness

        return backtracking(0, k)                                                                            #Return backtracking result from the start of cookies.
