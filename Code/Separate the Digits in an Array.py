class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:                                #Traverse nums.
            result.extend(int(d) for d in str(x))     #Separate each number to digits and append them to result.
        return result
