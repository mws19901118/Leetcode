class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n // 2) * ((m + 1) // 2) + ((n + 1) // 2) * (m // 2)      #Alice can only win if x + y is odd, so the result is even number count in [1, n] multiply odd number count in [1, m] plus odd number count in [1, n] multiply even number count in [1, m]. 
