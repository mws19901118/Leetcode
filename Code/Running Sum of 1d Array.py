class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]                    #Initialuze running sum with nums[0].
        for x in nums[1:]:                    #Traverse nums[1:].
            result.append(result[-1] + x)     #Calculate running sum and append it to result.
        return result                         #Return result.
