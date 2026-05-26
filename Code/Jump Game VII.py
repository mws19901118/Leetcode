class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp, prefix = [1] + [0] * (len(s) - 1), [1] + [0] * (len(s) - 1)                                              #Initialize dp and prefix. dp[i](1 for true and 0 for false) means if we can reach index i from index 0. prefix[i] is the prefix sum of dp[:i + 1].
        for i in range(1, len(s)):                                                                                   #Traverse from 1 to the end of s.
            if s[i] == "0":                                                                                          #If s[i] == '0', calulate the left and right bound of jumping to index i first.
                left, right = i - maxJump, i - minJump 
                dp[i] = int((0 if right < 0 else prefix[right]) - (0 if left <= 0 else prefix[left - 1]) > 0)        #If prefix[right] - prefix[left - 1] is greater than 0, it means at least 1 index in [left, right] can be reaches, so index i can be reached. We also need to handle the case left or right is out of bound.
            prefix[i] = prefix[i - 1] + dp[i]                                                                        #Update prefix[i].
        return bool(dp[-1])                                                                                          #Convert dp[-1] to bool and return it.
