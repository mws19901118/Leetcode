class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count = Counter(arr)                                                              #Count each number.
        return any((x and x * 2 in count) or (not x and count[x] > 1) for x in arr)       #Return true if there is a number which either is not 0 and has x * 2 in count or is 0 and its count is greater than 1.
