class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum, secondMaxNum = 0, 0
        for x in nums:                                        #Traverse nums to find the max number and second max number.
            if x > maxNum:
                secondMaxNum = maxNum
                maxNum = x
            elif x > secondMaxNum:
                secondMaxNum = x
        return (maxNum - 1) * (secondMaxNum - 1)              #Calculate max product.
