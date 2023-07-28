class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse = True)                                              #Sort batteries in descending order.
        extra = sum(batteries[n:])                                                  #All the batteries smaller than the n-th largest battery are extra power.
        for i in reversed(range(n)):                                                #Traverse the largest n battery in reverse order.
            if not i or extra // (n - i) < batteries[i - 1] - batteries[i]:         #If we reach the beginning or extra is not enought to fill gap any more and we cannot increase further pass batteries[i - 1].
                return batteries[i] + extra // (n - i)                              #Distribute them evenly to batteries[i:n], return that value plus batteries[i].
            extra -= (n - i) * (batteries[i - 1] - batteries[i])                    #Fill the gap for all batteries[i:n] to make them same as batteries[i - 1].
