class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        length = defaultdict(int)                        #Initialize the length of square streak ending at each number.
        result = 1                                       #Initialize result.
        for x in reversed(sorted(list(set(nums)))):      #Dedupe, sort and traverse from behind.
            length[x] = length[x ** 2] + 1               #length[x] is length[x ** 2] + 1.
            result = max(result, length[x])              #Update result.
        return result if result > 1 else -1              #Return result if it is greater than 1; otherwise, return -1.
