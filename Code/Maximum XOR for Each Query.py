class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1                #The max result of nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is always maximumBit bits of 1.
        xor = reduce(lambda x, y: x ^ y, nums)      #Calculate the XOR result of nums.
        result = []
        for x in reversed(nums):                    #Traverse nums backwards.
            result.append(xor ^ mask)               #K is xor ^ mask.
            xor ^= x                                #Remove x from xor.
        return result
