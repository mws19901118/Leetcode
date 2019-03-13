class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start, end = 0, len(letters) - 1
        while start <= end:                                                         #Binary search for the first letter larger than target.
            mid = (start + end) >> 1
            if letters[mid] > target and (mid == 0 or letters[mid - 1] <= target):  #If found, return it.
                return letters[mid]
            elif letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[0]                                                           #If not found, return the first letter in letters.
