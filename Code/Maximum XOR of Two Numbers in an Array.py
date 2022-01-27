class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result, mask = 0, 0
        for i in reversed(range(32)):                                   #Iterate starting from the first digit in binary representation of number and go to the right.
            mask |= 1 << i                                              #For each traversed digit we update our binary mask: in the beginning it is 10000...000, then it is 11000...000, 11100...000 and in the end 11111...111. We need this mask to quickly extract information about first several digits of our number.
            prefix = {num & mask for num in nums}                       #Create set of all possible first i digits of numbers, using num & mask: on the first iterations it will be first digit, on the next one first two digits and so on.
            start = result | 1 << i                               
            if any(start ^ prefix in found for prefix in prefix):       #Apply TwoSum problem: if we found two numbers with XOR starting with start, then we are happy.
                result = start                                          #Update result and break inner loop so we continue to look at the next digit.
        return result
