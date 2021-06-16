class Solution:
    def backtrack(self, matchsticks: List[int], target: int, sums: List[int], cache: dict) -> bool:
        t = sorted(sums)                                                                            #Sort sums.
        if (t[0], t[1], t[2], t[3]) in cache:                                                       #If current combination of sums is in cache, return the cached result.
            return cache[(t[0], t[1], t[2], t[3])]
        if not matchsticks:                                                                         #If no more match sticks, return true.
            return True
        result = False                                                                              #Initialize result to be false.
        for i in range(4):                                                                          #Try all 4 sides.
            if sums[i] + matchsticks[0] > target:                                                   #If current side plus current matchstick exeeds target side length, continue.
                continue
            sums[i] += matchsticks[0]                                                               #Add current matchstick to current side.
            if self.backtrack(matchsticks[1:], target, sums, cache):                                #Backtracking with remain sticks; if there is a solution, set result to true and break loop.
                result = True
                break
            sums[i] -= matchsticks[0]                                                               #Remove current matchstick from current side.
        cache[(t[0], t[1], t[2], t[3])] = result                                                    #Put result in cache.
        return result                                                                               #Return result.
    
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)                                                            #Sort matchsticks in descending order.
        total = sum(matchsticks)                                                                    #Compute the sum.
        target = total // 4                                                                         #Compute target side length.
        if len(matchsticks) < 4 or total % 4 or matchsticks[0] > target:                            #If matchsticks count is smaller than 4 or total cannot be divided by 4 or the first matchstick is longer than target side length, obviously cannot make a square.
            return False
        return self.backtrack(matchsticks, target, [0] * 4, {})                                     #Backtracking with 4 side lengths starting all at 0.
