class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda a, b: a | b, nums)                                                                  #Max OR is the OR of the entire list.

        @cache                                                                                                     #Cache result.
        def backtracking(index: int, current_or: int) -> int:                                                      #Backtracking with index and current or.
            if index == len(nums):                                                                                 #When reaches the end, if current or is same as max or, return 1; otherwise return 0.
                return 1 if current_or == max_or else 0
            return backtracking(index + 1, current_or) + backtracking(index + 1, current_or | nums[index])         #Return the sum of not taking nums[index] and taking nums[index].

        return backtracking(0, 0)                                                                                  #Return backtracking{0, 0).
