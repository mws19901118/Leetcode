class Solution:
    def minOperations(self, n: int) -> int:
        return (n - 1 - ((n - 1) // 2)) * ((n + 1) // 2)      #Since the operation does not change sum of array, the equal value is average of array, which is ((1 + 2 * (n - 1) + 1) * n // 2) // n = n.
                                                              #The target sum of first half(including middle) is n * ((n + 1) // 2).
                                                              #The actual sum of first half(including middle) is (1 + (n - 1) // 2 * 2 + 1) * ((n + 1) // 2) // 2 = (1 + ((n - 1) // 2)) * ((n + 1) // 2).
                                                              #So, minumin operation is n * ((n + 1) // 2) - (1 + ((n - 1) // 2)) * ((n + 1) // 2) = (n - 1 - ((n - 1) // 2)) * ((n + 1) // 2).
