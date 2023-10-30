class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: ("{0:b}".format(x).count('1'), x))          #Sort by count of 1 in binary and then by number itself.
