class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = 1 << len(nums)                                                #Galculate total numbers in given binary length.
        numberSet = set(int(x, 2) for x in nums)                          #Convert all binary numbers to int and store in a set.
        for i in range(1 << len(nums)):                                   #Traverse all numbers in given binary length.                                           
            if i not in numberSet:                                        #If i is not in numberSet, its binary string is a candidate.
                return format(i, '0' + str(len(nums)) + 'b')              #Convert i to binary string with same length and return.
