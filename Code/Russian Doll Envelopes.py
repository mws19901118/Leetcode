class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))       #Sort envelopes by width in asending order and then by height in desending order.
        dp = []                                             #Initialize dp. This list stores the height of a series of russian doll envelopes, so, it should be in asending order.
        for w, h in envelopes:                              #Traverse envelopes.
            index = bisect.bisect_left(dp, h)               #Binary search from left to find the place to insert h to dp.
            if index == len(dp):                            #If index is length of dp, current envelope is greater than all traversed envelop(because width is already sorted), append h to dp.
                dp.append(h)
            else:                                           #Otherwise, updated the height of dp[index] so the heigh is smaller and we hope in the future it's more likely to fit in another envelope.
                dp[index] = h
        return len(dp)                                      #Return the length of dp.
