class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(arr[i] & 1 and arr[i + 1] & 1 and arr[i + 2] & 1 for i in range(len(arr) - 2))      #Traverse arr and find.
