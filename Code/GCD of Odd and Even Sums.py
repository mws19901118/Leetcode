class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n      #Sum of first n odd number is (1 + 2 * n + 1) * n // 2 = n * (n + 1).
                      #Sum of first n even number is (2 * n) * n // 2 = n * n.
                      #So the GCD of n * (n + 1) and n * n is n.
