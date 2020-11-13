class Solution:
    def backtracking(self, nums: List[int], start: int) -> set:         #Return a set of tuples, representing the unique permutations of the numbers which appear after (including) the index "start".
        if start == len(nums) - 1:                                      #If start is the last element of nums, return it in tuple.
            return {(nums[start], )}
        s = set()
        for r in self.backtracking(nums, start + 1):                    #Generate new permutations by inserting the current element into different positions of r.
            for i in range(len(r) + 1):
                s.add(r[:i] + (nums[start], ) + r[i:])                  
        return s
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return [list(t) for t in self.backtracking(nums, 0)]            #Convert each tuple in set into a list and put them in a whole list.
