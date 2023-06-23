class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        subsequenceLength = [defaultdict(lambda: 1) for _ in range(len(nums))]                                                #Use default dict to store the arithmetic subsequence length by diff ending at current number. 
        result = 0                                                                                                            #Initialize result.
        for i, x in enumerate(nums):                                                                                          #Traverse nums.
            for j, y in enumerate(nums[:i]):                                                                                  #Traverse nums[:i].
                subsequenceLength[i][y - x] = max(subsequenceLength[j][y - x] + 1, subsequenceLength[i][y - x])               #Update subsequenceLength[i][y - x].
                result = max(result, subsequenceLength[i][y - x])                                                             #Update result.
        return result + 1
