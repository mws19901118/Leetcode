class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters, target) % len(letters)]                 #Binary search for the index of first letter larger than target and return the character at index after taking mod against length of letters.
