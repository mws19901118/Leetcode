class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dict={}
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                return True
        return False
