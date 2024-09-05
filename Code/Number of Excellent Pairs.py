class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))                                                              #De-dupe, as duplicate number doesn't matter.
        sortedNumberOfBits = sorted("{0:b}".format(x).count('1') for x in nums)             #Sort number of bits of each number.
        index, result = len(sortedNumberOfBits) - 1, 0                                      #Let's an excellent pair num1 and num2 share C common bits, while num1 has A bits not in num2 and num2 has B bits not in num1.
        for i in range(len(sortedNumberOfBits)):                                            #Then num1 & num2 has C bits and num1 | num2 has A + B + C bits, which is A + C + B + C bits in total, i.e. the number of bits of num1 and num2.
            while index >= 0 and sortedNumberOfBits[index] + sortedNumberOfBits[i] >= k:    #So, it converts tp a "2 sum greater than or equal to k" problem.
                index -= 1
            result += len(sortedNumberOfBits) - 1 - index
        return result
