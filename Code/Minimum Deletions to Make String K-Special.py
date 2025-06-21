class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        sorted_count = sorted(Counter(word).values())                                                #Count each character and sort the count.
        result, removed = inf, 0                                                                     #Initialize result and total removed characters whose count is smaller than current count.
        for i, x in enumerate(sorted_count):                                                         #Traverse sorted count.
            result = min(result, removed + sum(max(0, y - x - k) for y in sorted_count[i + 1:]))     #To make string k-special with current count as the smallest count, we have to first remove characters whose count is smaller than current count, then reduce other count to not greater than x + k.
            removed += x                                                                             #Add x to removed.
        return result
