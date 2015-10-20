class Solution:
    def perm(self, nums, start):                        #Return a set of tuples, representing the unique permutations of the numbers which appear after (including) the index "start".
        if start == len(nums)-1:                        #If start is the last element of nums, return it in tuple.
            return {(nums[start],)}
        s = set()
        for r in self.perm(nums, start+1):
            for i in range(len(nums)-start):
                s.add(r[:i]+(nums[start],)+r[i:])       #Generate new permutations by inserting the current element into different positions of r.
        return s
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums: return []
        return [list(t) for t in self.perm(nums, 0)]    #Convert each tuple in set into a list and put them in a whole list.
