class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @cache                                                                                                 #Cache result.
        def scoreDiff(i: int, j: int) -> int:                                                                  #Calculate the max score diff a player can get against the other player on nums[i:j + 1].
            return 0 if i > j else max(nums[i] - scoreDiff(i + 1, j), nums[j] - scoreDiff(i, j - 1))           #If i > j, return 0; otherwise, return the max diff of taking nums[i] or nums[j].
        return scoreDiff(0, len(nums) - 1) >= 0                                                                #Return the score diff for entire nums is greater than or equal to 0.
