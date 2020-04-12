class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        count = 0
        for x in arr:
            if (x + 1) in s:
                count += 1
        return count
