class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros, ones = [sum([1 for y in x if y == "0"]) for x in strs], [sum([1 for y in x if y == "1"]) for x in strs]                                        #Calculate the number of 0 and 1 respectively in each string.
        @cache                                                                                                                                                #Cache result.
        def dp(index: int, x: int, y: int):                                                                                                                   #DP to find the max subset in strs[index:] with x zeros and y ones allowed.                                                                          
            if index == len(strs):                                                                                                                            #If index reaches the end, return 0.
                return 0
            return max(dp(index + 1, x, y), (dp(index + 1, x - zeros[index], y - ones[index]) + 1) if x >= zeros[index] and y >= ones[index] else 0)          #Return the max of dp(index + 1, x, y) and dp(index + 1, x - zeros[index], y - ones[index]) + 1 if current string does not have more than x zeros or y ones.
        return dp(0, m, n)                                                                                                                                    #Return the result of dp(0, m, n).
