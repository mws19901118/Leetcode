class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        for i in range(len(num) - 2):                                    #Traverse all length 3 substrings.
            if num[i:i + 3] == num[i] * 3 and num[i:i + 3] > result:     #If it is of same digit and greater than result, update result.
                result = num[i:i + 3]
        return result
