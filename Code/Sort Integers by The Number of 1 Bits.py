class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x:(x.bit_count(), x))          #Sort by count of 1 in binary and then by number itself.
