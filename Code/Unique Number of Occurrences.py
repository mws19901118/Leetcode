class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        numberCount = Counter(arr)                                #Count each number.
        occurrenceCount = Counter(numberCount.values())           #Count each occurrence.
        return all(x == 1 for x in occurrenceCount.values())      #All occurrence should appear once.
