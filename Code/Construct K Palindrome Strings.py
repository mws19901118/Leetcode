class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)                                      #Count each character.
        odd_count = sum(int(x % 2) for x in count.values())     #Calculate the number of characters with odd count.
        return odd_count <= k and len(s) >= k                   #Odd count should not be greater than k and the length of s should not be smaller than k.
