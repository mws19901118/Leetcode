class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        prefixSum = [{x: 0 for x in '01234'}]                                                                #Initialize prefix sum for each digit.
        for x in s:                                                                                          #Traverse s and populate the prefix sum.
            prefixSum.append(deepcopy(prefixSum[-1]))
            prefixSum[-1][x] += 1
        result = -inf                                                                                        #Initialize result as negative infinity.
        for a, b in product('01234', '01234'):                                                               #Traverse each pair of a(odd count) and b(even count).
            if a == b:                                                                                       #If a and b are the same, skip.
                continue
            left = -1                                                                                        #Initialize the left of the sliding window, not inclusive.
            prevA, prevB = 0, 0                                                                              #Initialize the count of a and b in s[:left + 1] respectively.
            diffs = {(0, 0): inf, (0, 1): inf, (1, 0): inf, (1, 1): inf}                                     #Initialize the min diff of prevA - prevB based on the parity combination of a and b.
            for i, x in enumerate(s):                                                                        #Traverse s to check each right end of sliding window, inclusive.
                countA, countB = prefixSum[i + 1][a], prefixSum[i + 1][b]                                    #Get the count of a and b in s[:i + 1] respectively.
                while i - left >= k and countB - prevB >= 2 and countA - prevA >= 1:                         #Move forward left while the window size is at least k and count of a in the window is at least 1 and count of b in the window is at least 2.
                    diffs[(prevA & 1, prevB & 1)] = min(diffs[(prevA & 1, prevB & 1)], prevA - prevB)        #Update the min diff of the current parity combination of a and b if necessary.
                    left += 1
                    prevA, prevB = prefixSum[left + 1][a], prefixSum[left + 1][b]                            #Update prevA and prevB as left moving forward.
                if diffs[(1 - countA & 1, countB & 1)] != inf:                                               #To keep the count of a in the window as odd and the count of b in the window as even, find the min diff with parity of a which is the opposite of countA and parity of b which is the same of countB.
                    result = max(result, countA - countB - diffs[(1 - countA & 1, countB & 1)])              #Thus, countA - countB - diffs[(1 - countA & 1, countB & 1)] is the maximum difference between even and odd frequency in any substring ending at index i. Then update result if necessary.
        return result
