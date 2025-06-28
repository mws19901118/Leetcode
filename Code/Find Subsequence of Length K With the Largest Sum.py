class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_with_index = sorted([(x, i) for i, x in enumerate(nums)], reverse = True)      #Sort nums and keep index in desending order.
        indexes = set(i for _, i in nums_with_index[:k])                                    #Store the indexes of first k numbers in a set.
        return [x for i, x in enumerate(nums) if i in indexes]                              #Traverse nums and return the subsequence made by numbers on these indexes.
