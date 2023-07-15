class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()                                                                                            #Sort events by starting time.
        nextIndex = [bisect_left(events, [e + 1, 0, 0]) for s, e, v in events]                                   #For each event, find the index of next event with no conflict by binary search.

        @cache                                                                                                   #Cache result.
        def dp(index: int, x: int) -> int:                                                                       #DP to find the max value to attend x event in events[index:]
            if index == len(events) or not x:                                                                    #If index reaches the end or x == 0, return 0.
                return 0
            return max(dp(index + 1, x), events[index][2] + dp(nextIndex[index], x - 1))                         #Return the max of attending current event(events[index][2] + dp(nextIndex[index], x - 1)) and not attending current event(dp(index + 1, x)).

        return dp(0, k)                                                                                          #Return dp(0, k).
