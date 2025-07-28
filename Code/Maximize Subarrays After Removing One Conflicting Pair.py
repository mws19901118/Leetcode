class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        sortedConflictingPairs = sorted([sorted(x) for x in conflictingPairs], key = lambda x: x[1])          #Sort the normalized conflicting pairs(always a < b) by b in asending order.
        n += 1                                                                                                #Increase n.
        sortedConflictingPairs.append([n, n])                                                                 #Add a dummy conflicting pair [n, n] to the sorted conflicting pairs.
        maxGain = 0                                                                                           #Intialize the max gain on subarray count of removing a conflicting pair.
        maxLeft = 0                                                                                           #Initialize the largest left of visited conflicting pairs.
        invalid = 0                                                                                           #Initialize the total invalid subarrays without dropping any conflicting pair.
        secondMaxLeft = 0                                                                                     #Initialize the second largest left of visited conflicting pairs.
        secondInvalid = 0                                                                                     #Initialize the total invalid subarrays after dropping the worst conflicting pair.
        for left, right in sortedConflictingPairs:                                                            #Traverse sorted conflicting pairs.
            if left > maxLeft:                                                                                #Handle the scenario that current left is greater than maxLeft. The dummy conflicting pair will always trigger this scenario, so its purpose is to ensure calculating the maxGain of removing every conflicting pair whose left is current maxLeft.
                maxGain = max(maxGain, (secondMaxLeft - maxLeft) * (n - right) + invalid - secondInvalid)     #Calculate the gain of removing previous conflicting pair of maxLeft; then update maxGain if necessary. 
                secondInvalid = invalid                                                                       #Set secondInvalid to invalid.
                secondMaxLeft = maxLeft                                                                       #Set secondMaxLeft to maxLeft.
                invalid += (left - maxLeft) * (n - right)                                                     #There are (left - maxLeft) * (n - right) more invalid subarrays. For current pair, the invalid subarray count is (left + 1) * (n - right), but during calculation of previous maxLeft pair (maxLeft, rightOfMaxLeft), (maxLeft + 1) * (n - rightOfMaxLeft) is already added to invalid. And rightOfMaxLeft is not greater than current right, so we (maxLeft + 1) * (n - right) is already adde to invalid and we only need to add (left - maxLeft) * (n - right).
                maxLeft = left                                                                                #Update maxLeft.
            elif left > secondMaxLeft:                                                                        #Handle the scenario that current left is only greater than secondMaxLeft.
                secondInvalid += (left - secondMaxLeft) * (n - right)                                         #Comparing with secindMaxLeft, there are (left - secondMaxLeft) * (n - right) more invalid subarrays; same reason as line 16.
                secondMaxLeft = left                                                                          #Update secondMaxLeft.
        return (n - 1) * n // 2 - invalid + maxGain                                                           #There are (n - 1) * n // 2 total subarrays, because we increased original n by 1.
                                                                                                              #Next deduct invalid from total subarrays.
                                                                                                              #Then add maxGain to it.
