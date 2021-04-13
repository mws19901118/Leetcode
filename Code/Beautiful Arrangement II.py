class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        arrangement = [1]
        delta = k
        for i in range(k):                                      #Construct a subarray at the beginning with length k + 1, which is 1, k + 1, 2, k, 3, k - 1...
            arrangement.append(arrangement[-1] + delta)         #So, the distance between each adjacent number is k, k - 1, ..., 1.
            delta = -delta + 1 if delta > 0 else -delta - 1
        arrangement.extend([i for i in range(k + 2, n + 1)])    #Add the remaining, k + 2 to n, to list, so the distance between each adjacent number is 1 and already appeared.
        return arrangement
